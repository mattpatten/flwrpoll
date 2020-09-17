"""
	def __init__(self, *args, **kwargs):
		#The form is not expecting this kwarg to be passed in, so it must be popped off before calling super 
		#(i.e., basically initializing the otherwise unexpected variable)
		self.subjectID = kwargs.pop('subjectID', 998) #takes from self.flowerID (loaded from the view kwargs) and transfers it to this form (attaching it to the hiddeninput and thyus the model)
		super(RatingForm, self).__init__(*args, **kwargs) #loads up all the other variables as per norm
		print('RatingForm __init__')



	def get_form_kwargs(self, *args, **kwargs):
		#This method is what injects forms with their keyword arguments.
		#That is, from CheckConsentForm you can access the flower ID variable
		kwargs = super(ConsentView, self).get_form_kwargs() # grab the current set of form #kwargs

		if self.request.method == 'POST':
			request.session['participant'] = 11 #assign value to session key
			self.participantNumber = request.session.get('participant') #extract our value for this session and save it to a variable
			kwargs.update({'subjectID': self.participantNumber}) #inject into form
			
		return kwargs
		


	def get_form_kwargs(self, *args, **kwargs):
		#This method is what injects forms with their keyword (dictionary) arguments.
		#It is  passed into __init__ of the relevant form. You must pop the kwargs in init before calling super.
		#That is, from DemographicsForm you can access the subject ID variable
	
		kwargs = super(QuestionView, self).get_form_kwargs() # grab the current set of form #kwargs
		self.participantNumber = request.session.get('participant') #extract our value for this session and save it to a variable
		kwargs.update({'subjectID': self.participantNumber}) #inject into form	
		print('QuestionView get_form_kwargs')
		return kwargs


{% comment %}
Original jquery scripts used - updated so they work with touch-punch
<script src="http://code.jquery.com/jquery-3.4.1.js" integrity="sha256-WpOohJOqMqqyKL9FccASB9O0KwACQJpFTUBLTYOVvVU=" crossorigin="anonymous"></script>
<script src="http://code.jquery.com/ui/1.12.1/jquery-ui.js" integrity="sha256-T0Vest3yCU7pafRw9r+settMBX6JkKN06dqBnpQ8d30=" crossorigin="anonymous"></script>
{% endcomment %}

"""