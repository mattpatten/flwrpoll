from django.http      import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls      import reverse_lazy
from django.views     import generic
from django.db.models import Q, Max, Count
from django.conf      import settings

from django.contrib.staticfiles.utils   import get_files
from django.contrib.staticfiles.storage import StaticFilesStorage

from collections import Counter
from random import shuffle
import re
import boto3

from .all_images import get_image_filenames
from .parameter_instructions import instructions_text, get_verbose_field_name
from .models import Rating, Participant
from .forms import CheckConsentForm, DemographicsForm, RatingForm, AttentionForm



class BaseView(generic.ListView):
	template_name = 'polls/index.html'
	
	
	def get(self, request):

		querystring_source = self.request.GET.get('source','') #extract identifier from URL: /polls/?source=....
		querystring_id     = self.request.GET.get('id','') 	   #extract identifier from URL: /polls/?id=....

		if 'source_site' in self.request.session: #if there is a session variable already
			if querystring_source != '': #if we have new data to fill
				self.request.session['source_site'] = querystring_source #then fill it
		else: 
			self.request.session['source_site'] = querystring_source
			
		
		if 'linkID' in self.request.session: #if there is a session variable already
			if querystring_id != '': #if we have new data to fill
				self.request.session['linkID'] = querystring_id #then fill it
		else: 
			self.request.session['linkID'] = querystring_id
			

		if 'consent' not in self.request.session: 
			# Automatically redirect to consent page if they haven't provided consent as of yet
			return HttpResponseRedirect(reverse_lazy('polls:consent'))
		else:
			# Otherwise generate index page to ask whether to restart or continue session
			return render(request, self.template_name)



	def post(self, request):
	
		if 'session_restart' in request.POST: #user presses restart session button

			# Clear all session data
			if 'consent' 			 in self.request.session: del self.request.session['consent'];
			if 'participant' 		 in self.request.session: del self.request.session['participant'];
			if 'flowers_rated' 		 in self.request.session: del self.request.session['flowers_rated'];
			if 'flower_order' 		 in self.request.session: del self.request.session['flower_order'];
			if 'questions_completed' in self.request.session: del self.request.session['questions_completed'];
			if 'survey_finished' 	 in self.request.session: del self.request.session['survey_finished'];
			return HttpResponseRedirect(reverse_lazy('polls:consent'))

		elif 'session_continue' in request.POST: #user wants to continue session
			redirect_name = check_progress_and_redirect(self, request, 'base')
			if redirect_name is not None: #should always be true
				return HttpResponseRedirect(reverse_lazy(redirect_name))

		return render(request, self.template_name)



class ConsentView(generic.FormView):
	form_class = CheckConsentForm
	template_name = 'polls/consent.html'
	success_url = reverse_lazy('polls:demographics')
	initial = {'form': CheckConsentForm}


	def dispatch(self, request, *args, **kwargs):
		# Check that page is being loaded in correct order, and redirect if necessary. Otherwise load consent page as normal.
		if request.method == 'GET':
			redirect_name = check_progress_and_redirect(self, request, 'consent')
			if redirect_name is not None:
				return HttpResponseRedirect(reverse_lazy(redirect_name))

		return super(ConsentView, self).dispatch(request, *args, **kwargs)


	def form_valid(self, form):
		self.request.session['consent'] = True #store progress as a session variable
		return super(ConsentView, self).form_valid(form)



class DemographicsView(generic.FormView):
	form_class = DemographicsForm
	template_name = 'polls/demographics.html'
	success_url = reverse_lazy('polls:instructions')
	initial = {'form': DemographicsForm}


	def dispatch(self, request, *args, **kwargs):
		# Check that page is being loaded in correct order, and redirect if necessary. Otherwise load demographics page as normal.
		if request.method == 'GET':
			redirect_name = check_progress_and_redirect(self, request, 'demographics')
			if redirect_name is not None:
				return HttpResponseRedirect(reverse_lazy(redirect_name))
			
		return super(DemographicsView, self).dispatch(request, *args, **kwargs)


	def form_valid(self, form):
		# On successful form submission, also do the following extra tasks...
		
		# Save consent (from previous page) with this model using session variable
		if 'consent' in self.request.session: 
			form.instance.consent_given = self.request.session.get('consent')

		# Save link ID from SONA / survey host if provided
		if 'linkID' in self.request.session: 
			form.instance.linkID = self.request.session.get('linkID')

		# Save original site directed from, if provided
		if 'source_site' in self.request.session: 
			form.instance.source_site = self.request.session.get('source_site')

		# Check if user already has subject ID from previous session
		if 'participant' in self.request.session: 
			form.instance.subjectID_id = self.request.session.get('participant') #overwrite old data

		"""
		# Create subject ID for user
		if 'participant' not in self.request.session: 
			subject = Participant.objects.all().aggregate(id=(Max('subjectID')+1)) #lookup database of participants and increment largest participant number
			if not subject['id']: #if empty (i.e., first user on database)
				subject['id'] = 1
			self.request.session['participant'] = subject['id'] #store as session variable (so we can access this information from other pages/views)
			
		else: #if this session is continued
			subject = {'id': self.request.session.get('participant')} #get session variable and save for this subject's ID (i.e., participant number in database)
		
		form.instance.subjectID = subject['id'] #in both cases, save instance
		"""

		###########################
		#  Set up image ordering  #
		###########################

		session = boto3.Session(
			aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
			aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
		)
		
		#stimFilenames = get_image_filenames() #hack to read pre-generated image names from py file - if below fails to function
		
		#load from S3 bucket (make sure there are no special characters in the access key and password)
		stimFilenames = []
		s3 = session.resource('s3')
		my_bucket = s3.Bucket(settings.AWS_STORAGE_BUCKET_NAME)
		for obj in my_bucket.objects.filter(Prefix='static/polls/stimuli'):
			stimFilenames.append(obj.key)			

		# Loop through filenames and extract image numbers
		nums = []
		for filename in stimFilenames:
			nums.append(re.findall(r'\d+',filename)) #extract digits
		imgNum = [item for sublist in nums for item in sublist] #converts list of lists to a single list
		
		freq = {int(i):0 for i in imgNum} #initialize - full of zeros for all images

		"""
		# Query database to count number of times each of these images have been presented
		qs_flower_count = Rating.objects.values('flowerID').annotate(count=Count('pointiness')).order_by() 
		
		# Generate frequency histogram
		for db_flower in qs_flower_count: #for each flower that has ratings in the database
			if db_flower['flowerID'] in freq: #if this entry has a corresponding image file present
				freq[db_flower['flowerID']] = db_flower['count'] #add number of times its been rated to our frequency histogram
		"""
		
		# Randomize order of keys
		perm_freq_keys = list(freq.keys()) #get keys for dict and convert it to list (from iterable)
		shuffle(perm_freq_keys) #overwrites original array

		# Update order of dict to shuffled version
		# This is to make sure we select flowers randomly, rather than those with the highest index
		perm_freq = {}
		for key in perm_freq_keys:
			perm_freq.update({key:freq[key]})

		# Order by frequency and take the last x values (i.e., least common). Then extract image number only from the list pairs.
		self.request.session['flower_order'] = [img_num for img_num, img_freq in Counter(perm_freq).most_common()[:-(settings.MAX_TRIAL_NUM+1):-1]]
		#print([(img_num, img_freq) for img_num, img_freq in Counter(perm_freq).most_common()]) #display whole frequncy histogram
		#print(self.request.session.get('flower_order')) #display just the ones we're presenting to this user


		form.instance.flower_order = self.request.session.get('flower_order') #save flower order to model
		
		form.save()
		self.request.session['participant'] = form.instance.subjectID
		
		return super(DemographicsView, self).form_valid(form)

	

class InstructionsView(generic.TemplateView):
	template_name = 'polls/instructions.html'


	def dispatch(self, request, *args, **kwargs):
		# Check that page is being loaded in correct order, and redirect if necessary. Otherwise load instructions as normal
		if request.method == 'GET':
			redirect_name = check_progress_and_redirect(self, request, 'instructions')
			if redirect_name is not None:
				return HttpResponseRedirect(reverse_lazy(redirect_name))
			
		if request.method == 'POST':
			return redirect('polls:qs')
			
		return super(InstructionsView, self).dispatch(request, *args, **kwargs)


	def get_context_data(self, **kwargs):
		# Populate extra information to go into the HTML template.
		context = super().get_context_data(**kwargs)

		# If user has started rating flowers, update button label so they know they haven't lost any information
		if 'flowers_rated' not in self.request.session:
			button_label = 'Start survey'
		else:
			button_label = 'Return to survey'

		title,helptext = instructions_text() #load up strings describing the parameters from separate file

		context.update({
			'exemplars': ['0330','2280','1656','2037','0991','2271','2673','0397','2052','0691','0339','2200','1779','1600','2495'], 
			'button_label': button_label,
			'instructions_title': title,
			'instructions_text': helptext,
		})
		return context



class QuestionView(generic.CreateView):
	form_class = RatingForm
	template_name = 'polls/qs.html'
	get_success_url = reverse_lazy('polls:debrief') #new
	initial = {'form': RatingForm}


	def dispatch(self, request, *args, **kwargs):
		# Check that page is being loaded in correct order, and redirect if necessary. Otherwise load question page as normal
		if request.method == 'GET':
			redirect_name = check_progress_and_redirect(self, request, 'qs')
			if redirect_name is not None:
				return HttpResponseRedirect(reverse_lazy(redirect_name))
			
			# Intialize flowers rated counter
			if 'flowers_rated' not in self.request.session:
				self.request.session['flowers_rated'] = 0
				
			# Extract current flower to display from flower_order list
			self.flowerID = f"{self.request.session.get('flower_order')[self.request.session.get('flowers_rated')]:04d}"
			self.title = "buy" + self.flowerID + ".jpg"
			
			#TODO: ENABLE continue button

		return super(QuestionView, self).dispatch(request, *args, **kwargs)


	def get_context_data(self, **kwargs):
		# Populate extra information to go into the HTML template.
		context = super().get_context_data(**kwargs)
		context.update({
			'imageNum': self.flowerID, 
			'title': self.title,
			'current_flower': self.request.session.get('flowers_rated')+1,
			'total_flowers': settings.MAX_TRIAL_NUM,
		})
		context['form'].fields['flowerID'].initial = self.flowerID  #save generated image to model data
		return context

	
	def form_valid(self, form):
		# On successful form submission, also do the following extra tasks...
		
		if 'see_instructions' in self.request.POST: #user presses button to see instructions
			return HttpResponseRedirect(reverse_lazy('polls:instructions'))

		#otherwise, user has clicked button and wants to move on to next flower
		form.instance.subjectID_id = self.request.session.get('participant') #extract participant number from session information and save rating to database
		self.request.session['flowers_rated'] += 1 # Increment number of flowers rated

		return super(QuestionView, self).form_valid(form)


	def get_success_url(self):
		# Check if user has done enough trials, and get address for redirect
		if self.request.session.get('flowers_rated') >= settings.MAX_TRIAL_NUM:
			self.request.session['questions_completed'] = True
			return reverse_lazy('polls:debrief')
		else:
			return reverse_lazy('polls:qs')



class DebriefView(generic.CreateView):
	form_class = AttentionForm
	template_name = 'polls/debrief.html'
	get_success_url = reverse_lazy('polls:exit')
	initial = {'form': AttentionForm}


	def dispatch(self, request, *args, **kwargs):
		# Check that page is being loaded in correct order, and redirect if necessary. Otherwise load debrief page as normal.
		# This is important to ensure people don't skip the survey and go straight to the debrief page for their credit/money
		if request.method == 'GET':
			redirect_name = check_progress_and_redirect(self, request, 'debrief')
			if redirect_name is not None:
				return HttpResponseRedirect(reverse_lazy(redirect_name))
		
		return super(DebriefView, self).dispatch(request, *args, **kwargs)


	def get_success_url(self):

		#extract session variables
		linkID = self.request.session.get('linkID')
		source_site = self.request.session.get('source_site')
		
		#remove session variables from memory
		del self.request.session['linkID'];
		del self.request.session['source_site'];
	
		#If there is a survey link ID, we add this to the URL when we redirect from this page
		if source_site=='SONA':
			return 'https://uws.sona-systems.com/webstudy_credit.aspx?experiment_id=1340&credit_token=286a1d2fec494079beda12891828b4ef&survey_code=' + linkID
		elif source_site=='PROLIFIC':
			return 'https://app.prolific.co/submissions/complete?cc=66F80128' #return identifier for prolific
		else:
			return reverse_lazy('polls:exit') + '?source=' + source_site + '&id=' + linkID #return any other identifier



	def form_valid(self, form): 
		# On successful form submission, also do the following extra tasks...
		
		self.request.session['survey_finished'] = True 
		
		form.instance.subjectID_id = self.request.session.get('participant')
		
		# Count the number of times this user has entered the default value (i.e., not likely to have attempted the question) for each variable
		total_unresponsive = Rating.objects.filter(subjectID=form.instance.subjectID_id).aggregate(count=
			Count('appeal',  		   filter=Q(appeal__exact=5)) +
			Count('bullseye',  		   filter=Q(bullseye__exact=5)) +
			Count('busyness',  		   filter=Q(busyness__exact=5)) +
			Count('complexity',  	   filter=Q(complexity__exact=5)) +
			Count('depth',  		   filter=Q(depth__exact=5)) +
			Count('interest',  		   filter=Q(interest__exact=5)) +
			Count('petal_quantity',    filter=Q(petal_quantity__exact=5)) +
			Count('petal_size',		   filter=Q(petal_size__exact=5)) +
			Count('petal_variability', filter=Q(petal_variability__exact=5)) +
			Count('pointiness',  	   filter=Q(pointiness__exact=5)) +
			Count('symmetry',  		   filter=Q(symmetry__exact=5)) +
			Count('uniqueness',  	   filter=Q(uniqueness__exact=5))
		)
		form.instance.num_answers_unresponsive = total_unresponsive['count'] / (self.request.session['flowers_rated'] * settings.NUM_QUESTIONS_DISPLAYED) * 100
		
		return super(DebriefView, self).form_valid(form)



class ExitView(generic.TemplateView):
	template_name = 'polls/fin.html'




def check_progress_and_redirect(self, request, current_page):
	"""
	Check session variables to determine survey progress.
	The current_page is required so we don't redirect to same page in an endless loop
	Don't change the order - this specifically goes from the last page to the first so it doesn't redirect to an earlier page
	"""
	
	if 'survey_finished'        in self.request.session: return 'polls:exit'
	elif ('questions_completed' in self.request.session) and (current_page is not  'debrief'):     		  return 'polls:debrief'
	elif ('questions_completed' in self.request.session) and (current_page is      'debrief'):      	  return None
	elif ('participant'         in self.request.session) and (current_page not in ['instructions','qs']): return 'polls:instructions'
	elif ('participant'         in self.request.session) and (current_page in     ['instructions','qs']): return None
	elif ('consent'             in self.request.session) and (current_page is not  'demographics'): 	  return 'polls:demographics'
	elif ('consent'             in self.request.session) and (current_page is      'demographics'): 	  return None
	elif ('consent'         not in self.request.session) and (current_page is not  'consent'):      	  return 'polls:consent'
	elif ('consent'         not in self.request.session) and (current_page is      'consent'): 	   		  return None
	else: return None
