COPY (
	SELECT 
		"responseID",
		"subjectID_id",
		"flowerID",
		timestamp,
		appeal,
		bullseye,
		busyness,
		complexity,
		depth,
		interest,
		petal_quantity,
		petal_size,
		petal_variability,
		pointiness,
		symmetry,
		uniqueness
	FROM polls_rating
	ORDER BY "responseID"
)
To 'C:\MyFiles\Work\WSU\Neurofloristry\PostgreSQL\pg_output\all_ratings.csv' With CSV HEADER;