from django.contrib import admin
from django.db.models import Count

from .models import Participant, Rating, Attention


class RatingInline(admin.TabularInline):
	#Inlines are the display of these models inside individual participants
	model = Rating
	extra = 0
	readonly_fields = ('responseID','timestamp')
	fields = (
		'timestamp',
		'responseID',
		'subjectID',
		'flowerID',
		'appeal',
		'bullseye',
		'busyness',
		'complexity',
		'depth',
		'interest',
		'petal_quantity',
		'petal_size',
		'petal_variability',
		'pointiness',
		'symmetry',
		'uniqueness',
	)


class RatingAdmin(admin.ModelAdmin):
	# Display these fields on the home page of Rating model for these variables
	list_display = (
		'responseID',
		'subjectID',
		'flowerID',
		'appeal',
		'bullseye',
		'busyness',
		'complexity',
		'depth',
		'interest',
		'petal_quantity',
		'petal_size',
		'petal_variability',
		'pointiness',
		'symmetry',
		'uniqueness',
		'timestamp',
	)
	ordering = ('-subjectID','-responseID') # The field and direction (include - at start for descending) we want to sort database entries by
	search_fields = ['subjectID__subjectID','flowerID',]  # If you use the search function, the columns that it will search NB: Foreign keys need __name to be eligible for search
	list_per_page = 500

class AttentionInline(admin.TabularInline):
    #Inlines are the display of these models inside individual participants
	model = Attention
	extra = 0


class AttentionAdmin(admin.ModelAdmin):
	fields = ['subjectID','survey_attention','num_answers_unresponsive','comments'] 		# The fields to display when you click on an individual Attention model
	list_display = ('subjectID','survey_attention', 'num_answers_unresponsive', 'comments') # Display these fields on the home page of Attention model
	search_fields = ['subjectID__subjectID','survey_attention','num_answers_unresponsive','comments']  # If you use the search function, the columns that it will search
	ordering = ('-subjectID',) 																# The field and direction (include - at start for descending) we want to sort database entries by
	list_per_page = 250
	

class ParticipantAdmin(admin.ModelAdmin):
	# Used to break the page down into different segments (as an alternative to fields = ...)
	fieldsets = [
		('Demographics', {'fields': ['gender','age','country']}),
		('Experience',   {'fields': ['expertise_in_horticulture','expertise_in_floral_design','purchase_frequency']}),
		('Progress',     {'fields': ['consent_given','source_site','linkID','flower_order']}),
	]
	inlines = [AttentionInline, RatingInline] 																			# Include these other models within this model
	list_display = ('subjectID','gender','age','country','num_flowers_rated','source_site','linkID','consent_given',)	# Display field entries on the home page as a list for these variables
	search_fields = ['subjectID','gender','age','country','num_flowers_rated','source_site','linkID',] 					# If you use the search function, the columns that it will search
	ordering = ('-subjectID',)																							# The field and direction (include - at start for descending) we want to sort database entries by
	list_per_page = 250
	
	
	def get_queryset(self, request):
		# Add count of number of flowers rated on Participant object
		qs = super(ParticipantAdmin, self).get_queryset(request) #get all objects
		return qs.annotate(num_flowers_rated=Count('rating')) #count number of 'rating' foreign keys


	def num_flowers_rated(self, obj):
		# Allows sorting on num_flowers_rated column (otherwise it doesn't know what value to use)	
		return obj.num_flowers_rated
	num_flowers_rated.admin_order_field = 'num_flowers_rated'


# Generate admin site (must be placed after definition)
admin.site.register(Rating, RatingAdmin)
admin.site.register(Participant, ParticipantAdmin)
admin.site.register(Attention, AttentionAdmin)
