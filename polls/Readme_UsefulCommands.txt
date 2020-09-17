
Some useful commands that may help you if/when you're stuck:

Ctrl + Shift + R --> Hard reload (in Chrome). Reloads the website in full, including cache. If you make stylistic changes (e.g., in the CSS file), this may be the only way you'll see them.
http://localhost:8000/polls/ --> local address for website
http://localhost:8000/admin/polls/ --> local address for admin website

If you change a model variable (e.g., the default of appeal to be 7, or a new parameter called "fluffiness"), update the models.py then run makemigrations and migrate as below.


In the shell:
------------------
python manage.py runserver ---> Runs website that can be seen in a browser
python manage.py makemigrations ---> Creates the migrations that will be applied to model parameters and database (i.e., generates SQL commands)
python manage.py migrate ---> Performs the migrations specified through "makemigrations" (i.e., executes SQL commands)
python manage.py flush ---> Deletes all contents of database and superusers.
python manage.py createsuperuser ---> Allows for administrative access
python manage.py clearsessions ---> Clear all session data (variables that exist over multiple pages and are stored, like a server-side cookie to keep track of a single user)

vars(XXX) ---> Shows fields of variable/object XXX
print(XXX) ---> Prints value of object/field XXX

workon flwrpoll ---> Loads virtual environment

git show abc342cd ---> shows changes of the latest commit in command window

Create new project using template fles (commands need to be checked):
------------------
python django-admin startproject myproject
python manage.py startapp myapp 


In the code:
------------------
breakpoint() ---> Creates breakpoint where the code will pause at that line you can play with the variables in the shell (similarly, exit() and continue() )


Deployment
-------------------
git add . ---> Stages files to be committed
git commit -m "description of commit to be saved" ---> Commits files
git push origin master ---> updates github repository from files on local computer
eb deploy   ---> updates files on AWS server

git pull origin master ---> downloads files from github onto local computer

eb terminate --> Terminates environment, but not the application, to save instance hours.
eb create    --> (Re-)creates environment with the same configuration


Download database snapshot and import to PostgreSQL
See: https://stackoverflow.com/questions/6842393/import-sql-dump-into-postgresql-database
-------------------
(using text file format)
set PGPASSWORD=Psychology01
pg_dump -h aa33p3foyh3bx.cxlluqpbq2yy.ap-southeast-2.rds.amazonaws.com -U SSAP -d ebdb -f C:\MyFiles\Work\WSU\Neurofloristry\PostgreSQL\pg_snapshots\attributes2nd.sql
psql 	 -U postgres -c "SELECT pg_terminate_backend(pid) FROM pg_stat_activity WHERE datname = 'dbname';"      (remove other users from database connections)
dropdb 	 -U postgres dbname   	(drop database if one has been generated previously)
createdb -U postgres dbname		<or create table using psql command line: "CREATE DATABASE dbname;" or open pgAdmin4 and use GUI to create new database> 
psql 	 -U postgres -d dbname -f data_text.sql	
psql 	 -U postgres -d dbname -f query_XXXXX.sql



(using custom file format - not needed)
pg_dump -Fc -h aa33p3foyh3bx.cxlluqpbq2yy.ap-southeast-2.rds.amazonaws.com -U SSAP -d ebdb -f data_custom.sql
<create table using psql command line: "CREATE DATABASE dbname;" or open pgAdmin4 and use GUI to create new database> 
pg_restore -U postgres -d custom data_custom.sql
