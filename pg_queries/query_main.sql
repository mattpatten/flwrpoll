COPY (
	SELECT
		"flowerID",
		/* appeal */
		ROUND(AVG(appeal)::numeric,4) AS appeal_mean,
		ROUND(STDDEV(appeal)::numeric,4) AS appeal_sd,
		COUNT(appeal) AS appeal_count,

		/* bullseye */
		ROUND(AVG(bullseye)::numeric,4) AS bullseye_mean,
		ROUND(STDDEV(bullseye)::numeric,4) AS bullseye_sd,
		COUNT(bullseye) AS bullseye_count,

		/* busyness */
		ROUND(AVG(busyness)::numeric,4) AS busyness_mean,
		ROUND(STDDEV(busyness)::numeric,4) AS busyness_sd,
		COUNT(busyness) AS busyness_count,

		/* complexity */
		ROUND(AVG(complexity)::numeric,4) AS complexity_mean,
		ROUND(STDDEV(complexity)::numeric,4) AS complexity_sd,
		COUNT(complexity) AS complexity_count,

		/* depth */
		ROUND(AVG(depth)::numeric,4) AS depth_mean,
		ROUND(STDDEV(depth)::numeric,4) AS depth_sd,
		COUNT(depth) AS depth_count,

		/* interest */
		ROUND(AVG(interest)::numeric,4) AS interest_mean,
		ROUND(STDDEV(interest)::numeric,4) AS interest_sd,
		COUNT(interest) AS interest_count,


		/* petal quantity */
		ROUND(AVG(petal_quantity)::numeric,4) AS petal_quantity_mean,
		ROUND(STDDEV(petal_quantity)::numeric,4) AS petal_quantity_sd,
		COUNT(petal_quantity) AS petal_quantity_count,

		/* petal_size */
		ROUND(AVG(petal_size)::numeric,4) AS petal_size_mean,
		ROUND(STDDEV(petal_size)::numeric,4) AS petal_size_sd,
		COUNT(petal_size) AS petal_size_count,

		/* petal_variability */
		ROUND(AVG(petal_variability)::numeric,4) AS petal_variability_mean,
		ROUND(STDDEV(petal_variability)::numeric,4) AS petal_variability_sd,
		COUNT(petal_variability) AS petal_variability_count,

		/* pointiness */
		ROUND(AVG(pointiness)::numeric,4) AS pointiness_mean,
		ROUND(STDDEV(pointiness)::numeric,4) AS pointiness_sd,
		COUNT(pointiness) AS pointiness_count,

		/* symmetry */
		ROUND(AVG(symmetry)::numeric,4) AS symmetry_mean,
		ROUND(STDDEV(symmetry)::numeric,4) AS symmetry_sd,
		COUNT(symmetry) AS symmetry_count,

		/* uniqueness */
		ROUND(AVG(uniqueness)::numeric,4) AS uniqueness_mean,
		ROUND(STDDEV(uniqueness)::numeric,4) AS uniqueness_sd,
		COUNT(uniqueness) AS uniqueness_count

	FROM
		polls_rating
	GROUP BY
		"flowerID"
	ORDER BY
		"flowerID"
)
To 'C:\MyFiles\Work\WSU\Neurofloristry\PostgreSQL\pg_output\maindata.csv' With CSV HEADER;