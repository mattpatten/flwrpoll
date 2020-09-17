COPY (
SELECT 
	"subjectID", 
	min_resp_time,
	median_resp_time, 
	avg_resp_time,
	max_resp_time,
	total_time_min
FROM (
	SELECT 
		"subjectID",
		min(time_diff) as min_resp_time,
		percentile_disc(0.5) within group (order by time_diff) as median_resp_time,
		avg(time_diff) as avg_resp_time,
		max(time_diff) as max_resp_time,
		sum(time_diff)/60 as total_time_min
		FROM (
			SELECT 
				*,
				EXTRACT(epoch from timestamp - lag(timestamp) over (partition by "subjectID" order by timestamp asc)) as time_diff
			FROM polls_participant
			LEFT JOIN polls_rating
			ON polls_participant."subjectID" = polls_rating."subjectID_id"
		) t1
		GROUP BY "subjectID"
	) t2
ORDER BY "subjectID"
) 
To 'C:\MyFiles\Work\WSU\Neurofloristry\PostgreSQL\pg_output\resp_times.csv' With CSV HEADER;