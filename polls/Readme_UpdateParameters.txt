
To update a parameter (e.g., asking about the flower's 'symmetry' instead of 'pointiness'):
** FIRST - Get the name of the new variable to include from models.py file - e.g., 'appeal'
Place/update it:
 1) In forms > RatingForm, 'fields = ' 
 2) In forms > RatingForm, in widgets (and set as param1 or param2 depending if placed first or second onscreen).
 3) In views > DemographicsView > form_valid within the image ordering section, update database query: annotate(count=Count('-------')).order_by() with either one of the two new parameters.
 4) In instructions.html template, both sets of text within <li> tags
 5) In qs.html template: in div tag .... name="-------"
 6) In qs.html template: Inside tag {{ form.-------.label }}
In addition, update default value in models.py (None --> 5 for new parameter, 5 --> None for old parameter)


To add a new parameter, also do the following:
* Add field to Rating model
* In views > DebriefView > form_valid, add value count number of unresponsive answers.
* In parameter_instructions.py, add title and helptext that user sees on the instructions. 
* Add to admin.py in both RatingInline and RatingAdmin

In both cases - then perform [manage.py] makemigrations and migrate. This may collapse during deployment in a day or two, in which case you need to update the model in polls/migrations/0001_initial.py as well (or if you can, delete any files with a number higher than 0002)