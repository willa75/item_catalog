#Item Catalog Repo

Code for one of my full stack web developer nanodegree projects. *Recommeded to have [virtualenv](http://docs.python-guide.org/en/latest/dev/virtualenvs/)*

This was built for Udacity's fullstack nanodegree program:
An application that provides a list of items within a variety of categories as well as provide a user registration and authentication system. Registered users will have the ability to post, edit and delete their own items. To get started with the application follow the steps below:

1. Open Terminal/CMD and navigate to the directory of the project
2. (optional but recommended) Run `virtualenv env`
3. (optional but recommended) Run `source env/bin/activate`
4. Run `export WEBAPP_ENV="dev"`
5. Run `python manage.py setup_db` to create the db schema and close the python shell
6. Run `python manage.py server` to run the webserver and naviagte to the url in the browser.
7. Open web browser to http://localhost:5000/login to login to the site with credentials: 
	username: admin  
	password: password