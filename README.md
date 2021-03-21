# flask-test
## First create a database and table in postgresql. The tutorial gives a way to directly create a table using scripts, but it is not necessary for our bare-bone model. 
## create database testing;
## \c testing
## create table tests (id INT PRIMARY KEY,name VARCHAR (50),score INT);
## insert into tests (id,name,score) values (0,'Tuhin',100);

## For some reason, I had to create a user for my database, you may not have to do that if you have already done it
## sudo -u postgres -s createuser anish
## Then get into postgresql and type the folllowing:
## GRANT ALL PRIVILEGES ON TABLE tests TO anish;

## setting env variables
## export APP_SETTINGS="config.DevelopmentConfig"
## export DATABASE_URL="postgresql:///testing"
## Now run "python3 manage.py runserver" and your bare-bone webserver is up and running
## To view tuhin's marks in JSON format, use the url http://127.0.0.1:5000/get/1 (general format : http://127.0.0.1:5000/get/__id__)
## If you want to add a person's marks use the url http://127.0.0.1:5000/add?id=2&name=chirag&score=92
## For rest of information like which packages to download and any missing info can be found on the website https://medium.com/@dushan14/create-a-web-application-with-python-flask-postgresql-and-deploy-on-heroku-243d548335cc
