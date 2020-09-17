from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, int_list_validator
from .all_countries import country_list



class Consent(models.Model):

	terms_confirmed = models.BooleanField(
		default=False,
	)



class Participant(models.Model):
	
	subjectID = models.AutoField(
		"Subject Number",
		primary_key=True,
	)
	
	"""
	subjectID = models.PositiveIntegerField(
		"Subject Number",
		validators=[
			MinValueValidator(0)
		],
		primary_key=True, 
	) 
	"""
	
	consent_given = models.BooleanField(
		default=False,
	)

	flower_order = models.CharField(
		validators=[int_list_validator], 
		max_length=500,
		null=False,
		blank=False,
		default=None,
	)
	
	source_site = models.CharField(
		"Source website",
		max_length=20,
		null=True,
		blank=True,
		default=None,
	)
	
	linkID = models.CharField(
		"Survey Link ID",
		max_length=25,
		null=True,
		blank=True,
		default=None,
	)
	
	gender = models.CharField(
		max_length=10,
		choices=[
			('M','Male'),
			('F','Female'),
			('O','Other'),
			('P','Prefer not to say'),
		], 
		blank=False, 
		default=None,
	)
	
	age = models.PositiveIntegerField(
		validators=[
			MinValueValidator(16,"You must be 16 or over to participate in this experiment"), 
			MaxValueValidator(110,"Please enter your age."),
		], 
		null=False, 
		blank=False, 
		default=None,
	) 
	
	country = models.CharField(
		max_length=2, 
		choices=country_list,
		blank=False, 
	)
	
	expertise_in_horticulture  = models.PositiveIntegerField(
		"Horticultural Expertise",
		validators=[
			MinValueValidator(1,"Please select an option."), 
			MaxValueValidator(5,"Please select an option."),
		], 
		blank=False,
		default=0,
	)

	expertise_in_floral_design = models.PositiveIntegerField(
		"Floral Design Expertise",
		validators=[
			MinValueValidator(1,"You must select an option."), 
			MaxValueValidator(5,"You must select an option.")
		], 
		default=0, 
		blank=False,
	)
	
	purchase_frequency = models.CharField(
		max_length=10,
		choices=[
			('Never','Never'),
			('Quarterly','Once or twice in the space of several months'),
			('Monthly','Once or twice per month'),
			('Weekly','Once per week'),
			('Bi-weekly','Several times per week'),
		],
		blank=False, 
	)
	
	#what to send back when someone wants to view an instance of the model	
	def __str__(self):
		return str(self.subjectID)

	
	
class Rating(models.Model):
	
	responseID = models.AutoField(
		"Response ID",
		primary_key=True,
	)
	
	subjectID = models.ForeignKey(
		"Participant", 
		on_delete=models.CASCADE,
		verbose_name="Subject ID",
		null=False,
		blank=False,
	)
	
	flowerID = models.PositiveIntegerField(
		"Flower ID",
		validators=[
			MaxValueValidator(999999)
		],
		null=False,
		blank=False,
	)
	
	timestamp = models.DateTimeField(
		"Timestamp",
		auto_now_add=True,
		null=True, #required to perform makemigrations
		blank=False,
	)
	
	appeal = models.PositiveIntegerField(
		"Appeal",     #verbose name of field (if you want to specify something different from the field name)
		validators=[
			MaxValueValidator(10),
		],
		null=True,    #if null values are allowed as valid entries
		blank=True,   #if the field is allowed to be left blank during form submission
		default=5, #add default if measure is being displayed in survey, otherwise set as None
	)
	
	bullseye = models.PositiveIntegerField(
		"Bullseye",
		validators=[
			MaxValueValidator(10),
		],
		null=True,
		blank=True,
		default=None, 
	)

	busyness = models.PositiveIntegerField(
		"Busyness",
		validators=[
			MaxValueValidator(10),
		],
		null=True,
		blank=True,
		default=None,
	)

	complexity = models.PositiveIntegerField(
		"Complexity",
		validators=[
			MaxValueValidator(10),
		],
		null=True,
		blank=True,
		default=None,
	)

	depth = models.PositiveIntegerField(
		"Flower depth",
		validators=[
			MaxValueValidator(10),
		],
		null=True,
		blank=True,
		default=None,
	)
	
	interest = models.PositiveIntegerField(
		"Visual Interest", #verbose name of field (if you want to specify something different from the field name)
		validators=[
			MaxValueValidator(10),
		],
		null=True,    #if null values are allowed as valid entries
		blank=True,   #if the field is allowed to be left blank during form submission
		default=5, #add default if measure is being displayed in survey, otherwise set as None
	)
	
	petal_quantity = models.PositiveIntegerField(
		"Quantity of Petals",
		validators=[
			MaxValueValidator(10),
		],
		null=True,
		blank=True,
		default=None,
	)

	petal_size = models.PositiveIntegerField(
		"Petal size",
		validators=[
			MaxValueValidator(10),
		],
		null=True,
		blank=True,
		default=None,
	)
	
	petal_variability = models.PositiveIntegerField(
		"Petal variability",
		validators=[
			MaxValueValidator(10),
		],
		null=True,
		blank=True,
		default=None,
	)

	pointiness = models.PositiveIntegerField(
		"Pointiness",
		validators=[
			MaxValueValidator(10),
		],
		null=True,
		blank=True,
		default=None,
	)

	symmetry = models.PositiveIntegerField(
		"Symmetry",
		validators=[
			MaxValueValidator(10),
		],
		null=True,
		blank=True,
		default=None,
	)

	uniqueness = models.PositiveIntegerField(
		"Uniqueness",
		validators=[
			MaxValueValidator(10),
		],
		null=True,
		blank=True,
		default=None,
	)

	#what to send back when someone wants to view an instance of the model
	def __str__(self):
		if self.responseID==None:
			return "ERROR - No response ID"
		return str(self.responseID)



class Attention(models.Model):

	#This is a special case of foreign key where things link up one-to-one with a different model. Here, each participant provides one attention rating only.
	subjectID = models.OneToOneField( 
		"Participant", 
		primary_key=True,
		on_delete=models.CASCADE, #if we delete the participant from the database, delete the associated Attention object as well.
		verbose_name="Subject ID",
		related_name="sID",
		null=False,
		blank=False,
	)

	survey_attention = models.PositiveIntegerField(
		validators=[
			MaxValueValidator(10)
		],
		choices=[(i,i) for i in range(1,11)], #same as [(1,1), (2,2), (3,3) .... ]
		null=True, 
		default=None,
	)
	
	comments = models.CharField(
		max_length=500, 
		null=True, 
		default=None,
		blank=True,
	)
	
	num_answers_unresponsive = models.DecimalField(
		"Unresponsive (%)",
		validators=[
			MinValueValidator(0),
			MaxValueValidator(100),
		],
		max_digits=3, #including decimal places
		decimal_places=0,
		null=True,
		default=None,
		blank=True,
	)

	#what to send back when someone wants to view an instance of the model	
	def __str__(self):
		return str(self.subjectID)