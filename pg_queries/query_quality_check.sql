COPY (
SELECT 
	"subjectID",
	consent_given,
	flower_order,
	source_site,
	"linkID",
	gender,
	age,
	country,
	expertise_in_horticulture,
	expertise_in_floral_design,
	purchase_frequency,	

	EXTRACT(EPOCH FROM (max(timestamp) - min(timestamp))/60) as total_time,
	ROUND(avg(survey_attention)::numeric,0) as attention,
	ROUND(avg(num_answers_unresponsive)::numeric,0) as unresponsive,

	/* appeal */
	min(appeal)					as appeal_min,
	max(appeal)					as appeal_max,
	avg(appeal)					as appeal_avg,
	stddev(appeal) 				as appeal_sd,

	/* bullseye */
	min(bullseye)				as bullseye_min,
	max(bullseye)				as bullseye_max,
	avg(bullseye)				as bullseye_avg,
	stddev(bullseye) 			as bullseye_sd,
	
	/* busyness */
	min(busyness)				as busyness_min,
	max(busyness)				as busyness_max,
	avg(busyness)				as busyness_avg,
	stddev(busyness) 			as busyness_sd,
	
	/* complexity */
	min(complexity)				as complexity_min,
	max(complexity)				as complexity_max,
	avg(complexity)				as complexity_avg,
	stddev(complexity) 			as complexity_sd,
	
	/* depth */
	min(depth)					as depth_min,
	max(depth)					as depth_max,
	avg(depth)					as depth_avg,
	stddev(depth) 				as depth_sd,

	/* interest */
	min(interest)				as interest_min,
	max(interest)				as interest_max,
	avg(interest)				as interest_avg,
	stddev(interest) 			as interest_sd,
	
	/* petal_quantity */
	min(petal_quantity)			as petal_quantity_min,
	max(petal_quantity)			as petal_quantity_max,
	avg(petal_quantity)			as petal_quantity_avg,
	stddev(petal_quantity) 		as petal_quantity_sd,
	
	/* petal_size */
	min(petal_size)				as petal_size_min,
	max(petal_size)				as petal_size_max,
	avg(petal_size)				as petal_size_avg,
	stddev(petal_size) 			as petal_size_sd,
	
	/* petal_variability */
	min(petal_variability)		as petal_variability_min,
	max(petal_variability)		as petal_variability_max,
	avg(petal_variability)		as petal_variability_avg,
	stddev(petal_variability) 	as petal_variability_sd,
	
	/* pointiness */
	min(pointiness)				as pointiness_min,
	max(pointiness)				as pointiness_max,
	avg(pointiness)				as pointiness_avg,
	stddev(pointiness) 			as pointiness_sd,
	
	/* symmetry */
	min(symmetry)				as symmetry_min,
	max(symmetry)				as symmetry_max,
	avg(symmetry)				as symmetry_avg,
	stddev(symmetry) 			as symmetry_sd,
	
	/* uniqueness */
	min(uniqueness)				as uniqueness_min,
	max(uniqueness)				as uniqueness_max,
	avg(uniqueness)				as uniqueness_avg,
	stddev(uniqueness) 			as uniqueness_sd

FROM polls_participant
LEFT JOIN polls_rating
ON polls_participant."subjectID" = polls_rating."subjectID_id"

LEFT JOIN polls_attention
ON polls_participant."subjectID" = polls_attention."subjectID_id"

GROUP BY polls_participant."subjectID"
ORDER BY "subjectID"
) 
To 'C:\MyFiles\Work\WSU\Neurofloristry\PostgreSQL\pg_output\quality_check.csv' With CSV HEADER;