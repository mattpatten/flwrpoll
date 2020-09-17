:: Set password so it doesn't ask us after each invoke of PostgreSQL
::set PGPASSWORD=

:: Download database from AWS server
pg_dump -h aa33p3foyh3bx.cxlluqpbq2yy.ap-southeast-2.rds.amazonaws.com -U SSAP -d ebdb -f C:\MyFiles\Work\WSU\Neurofloristry\PostgreSQL\pg_snapshots\attributes_and_appeal.sql

:: Cut off any current users who are accessing the database (there's an issue with PostgreSQL where this occurs more frequently than it should)
:: And then drop current database and all its data (a hack because it's not easy to append to an existing database)
:: If you're downloading the data for the first time you should skip these two lines and just start by creating the database
psql -U postgres -c "SELECT pg_terminate_backend(pid) FROM pg_stat_activity WHERE datname = 'aws_flwrpoll';"
dropdb -U postgres aws_flwrpoll

:: Create database to be saved to
createdb -U postgres aws_flwrpoll

:: Import data from the file we downloaded to our freshly created database
psql -U postgres -d aws_flwrpoll -f C:\MyFiles\Work\WSU\Neurofloristry\PostgreSQL\pg_snapshots\attributes_and_appeal.sql

:: Run our queries and output to file
psql -U postgres -d aws_flwrpoll -f C:\MyFiles\Work\WSU\Neurofloristry\PostgreSQL\pg_queries\query_main.sql
psql -U postgres -d aws_flwrpoll -f C:\MyFiles\Work\WSU\Neurofloristry\PostgreSQL\pg_queries\query_demographics.sql
psql -U postgres -d aws_flwrpoll -f C:\MyFiles\Work\WSU\Neurofloristry\PostgreSQL\pg_queries\query_all_ratings.sql
psql -U postgres -d aws_flwrpoll -f C:\MyFiles\Work\WSU\Neurofloristry\PostgreSQL\pg_queries\query_attention.sql
psql -U postgres -d aws_flwrpoll -f C:\MyFiles\Work\WSU\Neurofloristry\PostgreSQL\pg_queries\query_quality_check.sql
psql -U postgres -d aws_flwrpoll -f C:\MyFiles\Work\WSU\Neurofloristry\PostgreSQL\pg_queries\query_resp_times.sql
psql -U postgres -d aws_flwrpoll -f C:\MyFiles\Work\WSU\Neurofloristry\PostgreSQL\pg_queries\query_props_appeal.sql
psql -U postgres -d aws_flwrpoll -f C:\MyFiles\Work\WSU\Neurofloristry\PostgreSQL\pg_queries\query_props_interest.sql
