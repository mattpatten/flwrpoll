from .models import Rating

def instructions_text():
	title = {
		'appeal'			: get_verbose_field_name(Rating,'appeal'),
		'bullseye'		    : get_verbose_field_name(Rating,'bullseye'),
		'busyness'		    : get_verbose_field_name(Rating,'busyness'),
		'complexity' 		: get_verbose_field_name(Rating,'complexity'),
		'depth' 	    	: get_verbose_field_name(Rating,'depth'),
		'interest'			: get_verbose_field_name(Rating,'interest'),
		'petal_quantity'    : get_verbose_field_name(Rating,'petal_quantity'),
		'petal_size' 		: get_verbose_field_name(Rating,'petal_size'),
		'petal_variability' : get_verbose_field_name(Rating,'petal_variability'),
		'pointiness'		: get_verbose_field_name(Rating,'pointiness'),
		'symmetry'			: get_verbose_field_name(Rating,'symmetry'),
		'uniqueness' 		: get_verbose_field_name(Rating,'uniqueness'),
	}
	helptext = {
		'appeal'			: 'How appealing do you find the flower? (0 extremely unappealing - 10 extremely appealing)',
		'bullseye'		    : 'Does the flower resemble a bullseye? Does it contain patterns of alternating colours? (0 a single colour – 10 a clear bullseye pattern)',
		'busyness'		    : 'Is there a lot of fine detail in this flower? (0 little detail – 10 very detailed)',
		'complexity' 		: 'The complexity of the flower’s appearance. (0 not at all complex – 10 extremely complex)',
		'depth' 	    	: 'How many layers of petals are there and does the flower appear thin and shallow, or have more depth? (0 only a single layer, very thin – 10 many layers, lots of depth)',
		'interest'			: 'Separately from how much you like the flower, you may find the look of the flower \'interesting\'. Do you find the flower visually interesting? (0 very boring - 10 very interesting)',
		'petal_quantity'    : 'How many petals are in the flower? (0 not many at all – 10 lots of petals)',
		'petal_size' 		: 'The average size of the petals in the flower. (0 very small petals – 10 very large petals)',
		'petal_variability' : 'Are petals consistently the same size and shape, or are there large differences between petals? (0 all petals are the same – 10 many petals are different from each other)',
		'pointiness'  		: 'How pointy are the edges of the petals? (0 extremely rounded – 10 extremely pointy)',
		'symmetry' 		    : 'Is the flower symmetrical? Consider both the inside and the outline. (0 extremely irregular – 10 extremely symmetric)',
		'uniqueness' 		: 'How unique do you find the look of the flower? (0 not at all unique – 10 extremely unique)',
	}
	return title,helptext
	
	
def get_verbose_field_name(self,field_name):
	# Gets verbose name of the specific field 'field_name' specified in the model
	return self._meta.get_field(field_name).verbose_name
