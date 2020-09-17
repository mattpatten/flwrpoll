COPY (
WITH t0 AS
(
	SELECT 
		"subjectID_id",
		ROUND((cast(COUNT(*) as decimal)/70*100)::numeric,0) as prop_0
	FROM polls_rating
	WHERE interest=0
	GROUP BY "subjectID_id"
),
t1 AS
(
	SELECT 
		"subjectID_id",
		ROUND((cast(COUNT(*) as decimal)/70*100)::numeric,0) as prop_1
	FROM polls_rating
	WHERE interest=1
	GROUP BY "subjectID_id"
),
t2 AS
(
	SELECT 
		"subjectID_id",
		ROUND((cast(COUNT(*) as decimal)/70*100)::numeric,0) as prop_2
	FROM polls_rating
	WHERE interest=2
	GROUP BY "subjectID_id"
),
t3 AS
(
	SELECT 
		"subjectID_id",
		ROUND((cast(COUNT(*) as decimal)/70*100)::numeric,0) as prop_3
	FROM polls_rating
	WHERE interest=3
	GROUP BY "subjectID_id"
),
t4 AS
(
	SELECT 
		"subjectID_id",
		ROUND((cast(COUNT(*) as decimal)/70*100)::numeric,0) as prop_4
	FROM polls_rating
	WHERE interest=4
	GROUP BY "subjectID_id"
),
t5 AS 
(
	SELECT 
		"subjectID_id",
		ROUND((cast(COUNT(*) as decimal)/70*100)::numeric,0) as prop_5
	FROM polls_rating
	WHERE interest=5
	GROUP BY "subjectID_id"
),
t6 AS 
(
	SELECT 
		"subjectID_id",
		ROUND((cast(COUNT(*) as decimal)/70*100)::numeric,0) as prop_6
	FROM polls_rating
	WHERE interest=6
	GROUP BY "subjectID_id"
),
t7 AS 
(
	SELECT 
		"subjectID_id",
		ROUND((cast(COUNT(*) as decimal)/70*100)::numeric,0) as prop_7
	FROM polls_rating
	WHERE interest=7
	GROUP BY "subjectID_id"
),
t8 AS 
(
	SELECT 
		"subjectID_id",
		ROUND((cast(COUNT(*) as decimal)/70*100)::numeric,0) as prop_8
	FROM polls_rating
	WHERE interest=8
	GROUP BY "subjectID_id"
),
t9 AS 
(
	SELECT 
		"subjectID_id",
		ROUND((cast(COUNT(*) as decimal)/70*100)::numeric,0) as prop_9
	FROM polls_rating
	WHERE interest=9
	GROUP BY "subjectID_id"
),
t10 AS 
(
	SELECT 
		"subjectID_id",
		ROUND((cast(COUNT(*) as decimal)/70*100)::numeric,0) as prop_10
	FROM polls_rating
	WHERE interest=10
	GROUP BY "subjectID_id"
)

SELECT
	polls_participant."subjectID",
	COALESCE(t0.prop_0,0) AS prop0,
	COALESCE(t1.prop_1,0) AS prop1,
	COALESCE(t2.prop_2,0) AS prop2,
	COALESCE(t3.prop_3,0) AS prop3,
	COALESCE(t4.prop_4,0) AS prop4,
	COALESCE(t5.prop_5,0) AS prop5,
	COALESCE(t6.prop_6,0) AS prop6,
	COALESCE(t7.prop_7,0) AS prop7,
	COALESCE(t8.prop_8,0) AS prop8,
	COALESCE(t9.prop_9,0) AS prop9,
	COALESCE(t10.prop_10,0)  AS prop10
FROM polls_participant
LEFT JOIN t0 ON t0."subjectID_id"=polls_participant."subjectID"
LEFT JOIN t1 ON t1."subjectID_id"=polls_participant."subjectID"
LEFT JOIN t2 ON t2."subjectID_id"=polls_participant."subjectID"
LEFT JOIN t3 ON t3."subjectID_id"=polls_participant."subjectID"
LEFT JOIN t4 ON t4."subjectID_id"=polls_participant."subjectID"
LEFT JOIN t5 ON t5."subjectID_id"=polls_participant."subjectID"
LEFT JOIN t6 ON t6."subjectID_id"=polls_participant."subjectID"
LEFT JOIN t7 ON t7."subjectID_id"=polls_participant."subjectID"
LEFT JOIN t8 ON t8."subjectID_id"=polls_participant."subjectID"
LEFT JOIN t9 ON t9."subjectID_id"=polls_participant."subjectID"
LEFT JOIN t10 ON t10."subjectID_id"=polls_participant."subjectID"
ORDER BY polls_participant."subjectID"
) 
To 'C:\MyFiles\Work\WSU\Neurofloristry\PostgreSQL\pg_output\props_interest.csv' With CSV HEADER;


/*
COPY (
WITH t5 AS 
(
	SELECT 
		"subjectID_id",
		ROUND((cast(COUNT(*) as decimal)/70*100)::numeric,0) as prop_5
	FROM polls_rating
	WHERE interest=5
	GROUP BY "subjectID_id"
),
t10 AS 
(
	SELECT 
		"subjectID_id",
		COALESCE(ROUND((cast(COUNT(*) as decimal)/70*100)::numeric,0),0) as prop_10
	FROM polls_rating
	WHERE interest=10
	GROUP BY "subjectID_id"
)

SELECT
	polls_participant."subjectID",
	t5.prop_5,
	t10.prop_10
FROM polls_participant
LEFT JOIN t5 ON t5."subjectID_id"=polls_participant."subjectID"
LEFT JOIN t10 ON t10."subjectID_id"=polls_participant."subjectID"
ORDER BY polls_participant."subjectID"
) 
To 'C:\MyFiles\Work\WSU\Neurofloristry\PostgreSQL\pg_output\props.csv' With CSV HEADER;
*/


/*
COPY (
	SELECT 
		"subjectID_id",
		ROUND((cast(COUNT(*) as decimal)/70*100)::numeric,0) as prop_10
	FROM polls_rating
	WHERE interest=10
	GROUP BY "subjectID_id"
	ORDER BY "subjectID_id"
) 
To 'C:\MyFiles\Work\WSU\Neurofloristry\PostgreSQL\pg_output\props.csv' With CSV HEADER;
*/