from django.urls 				import path, re_path
from django.views.generic.base 	import RedirectView
from django.conf      			import settings
from django.conf.urls.static 	import static
from . import views

app_name = 'polls'
urlpatterns = [
	path('consent/',      		  views.ConsentView.as_view(),      name='consent'), 	  								# /polls/consent/
	path('demographics/', 		  views.DemographicsView.as_view(), name='demographics'), 								# /polls/demographics/
	path('instructions/', 		  views.InstructionsView.as_view(), name='instructions'), 								# /polls/instructions/
	path('qs/',           		  views.QuestionView.as_view(),     name='qs'), 		  								# /polls/qs/
	path('debrief/',      		  views.DebriefView.as_view(),      name='debrief'), 	  								# /polls/debrief/
	path('fin/', 		  		  views.ExitView.as_view(),  		name='exit'),   									# /polls/fin/
	path('lab/',          		  RedirectView.as_view(url='https://neuroflorist.org/', permanent=False), name='lab'), 	# /polls/lab/
	re_path(r'^.*$',   	  		  views.BaseView.as_view(),         name='base'),         								# /polls/<ANYTHING> any other page gets directed to the index
] #+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)