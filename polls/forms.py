from django import forms
from .models import Consent, Participant, Rating, Attention
from django.utils.safestring import mark_safe


class CheckConsentForm(forms.ModelForm):
	class Meta:
		model = Consent
		fields = ['terms_confirmed']	
		widgets = {
			'terms_confirmed': forms.CheckboxInput(attrs={'required':True}), #user cannot proceed without checking the box
		}
		labels = {
			'terms_confirmed': 'I give my consent to participate in this experiment',
		}



class DemographicsForm(forms.ModelForm):
	class Meta:
		model = Participant
		fields = ['gender', 'age', 'country', 'expertise_in_horticulture', 'expertise_in_floral_design', 'purchase_frequency',]
		#exclude = ['subjectID', 'consent_given', 'linkID', 'flower_order',]
		widgets = {
			'age': forms.TextInput(attrs={'id':'age-textbox',}), #for CSS layout
			'gender': forms.RadioSelect(),
			'country': forms.Select(attrs={'id':'country-dropdown'}), #for CSS layout
			'expertise_in_horticulture': forms.HiddenInput(attrs={'id':'hort_rating', 'type':'range', 'step':'1', }), 
			'expertise_in_floral_design': forms.HiddenInput(attrs={'id':'floral_design_rating', 'type':'range', 'step':'1', }),
			'purchase_frequency': forms.Select(attrs={'id':'purchase-freq-dropdown'}), #for CSS layout
		}
		labels = {
			'age': 'Age: ',
			'gender': 'Gender: ',
			'country': 'Country of residence: ',
			'expertise_in_horticulture': mark_safe('Please state your experience in <i>horticulture</i>: '),
			'expertise_in_floral_design': mark_safe('Please state your experience in <i>floral design</i>: '),
			'purchase_frequency': 'How often do you buy flowers?',
		}
		error_messages = {
			'age': {'invalid':'Please enter your age.',},
		}
	
	
	def clean_expertise_in_horticulture(self):
		user_val = self.cleaned_data.get('expertise_in_horticulture') #get user value
		self.fields['expertise_in_horticulture'].initial = user_val   #set as new initial value so when page repopulates, it places what the user has already specified
		return user_val #always return a value to use as the cleaned data version


	def clean_expertise_in_floral_design(self):
		user_val = self.cleaned_data.get('expertise_in_floral_design')
		self.fields['expertise_in_floral_design'].initial = user_val
		return user_val


		
class RatingForm(forms.ModelForm):
	class Meta:
		model = Rating
		fields = ['flowerID','appeal','interest',] #excluding ['subjectID','timestamp',... and blocked out parameters below]
		
		#link the javascript id to a hidden input within our form so the slider value saves to this model variable
		widgets = { 
			'flowerID'			:forms.HiddenInput(),
			'appeal'  			:forms.HiddenInput(attrs={'id': 'param1_value',}), 
			#'bullseye'			:forms.HiddenInput(attrs={'id': 'param1_value',}), 
			#'busyness'			:forms.HiddenInput(attrs={'id': 'param2_value',}), 
			#'complexity'		:forms.HiddenInput(attrs={'id': 'param2_value',}), 
			#'depth'			:forms.HiddenInput(attrs={'id': 'param1_value',}), 
			'interest'  		:forms.HiddenInput(attrs={'id': 'param2_value',}),
			#'petal_quantity'	:forms.HiddenInput(attrs={'id': 'param1_value',}), 
			#'petal_size'		:forms.HiddenInput(attrs={'id': 'param1_value',}), 
			#'petal_variability':forms.HiddenInput(attrs={'id': 'param1_value',}), 
			#'pointiness'		:forms.HiddenInput(attrs={'id': 'param1_value',}),
			#'symmetry'			:forms.HiddenInput(attrs={'id': 'param2_value',}),
			#'uniqueness'		:forms.HiddenInput(attrs={'id': 'param2_value',}), 
		}

	
		
class AttentionForm(forms.ModelForm):
	class Meta:
		model = Attention
		fields = ['survey_attention','comments']
		#exclude = ['subjectID','num_answers_unresponsive']
		widgets = {
			'survey_attention': forms.RadioSelect(),
			'comments': forms.Textarea(attrs={'id': 'comments_textbox',}), #for CSS layout
		}
		labels = {
			'survey_attention': 'Before going, please rate how much attention you devoted to this survey (1 - almost no attention, 10 - full attention). We will not reject your work based on your answer to this question.',
			'comments': 'Please let us know of any comments you have about the questionnaire or website here (optional): '
		}
		
	
	def __init__(self, *args, **kwargs):
		super(AttentionForm, self).__init__(*args, **kwargs)
		self.fields['survey_attention'].required = False  #must put this here so it comes unselected on page-load
		self.fields['comments'].required = False          #must put this here so it comes unselected on page-load