COPY (
	SELECT *
	FROM polls_participant
) 
To 'C:\MyFiles\Work\WSU\Neurofloristry\PostgreSQL\pg_output\demographics.csv' With CSV HEADER;