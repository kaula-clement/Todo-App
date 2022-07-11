# Todo-App
Todo app api with user authentication and javascript
user registration
login
logout
add todo
delete todo

# installation
After you cloned the repository, you want to create a virtual environment, so you have a clean python installation. You can do this by running the command

*python -m venv env* :|Virtual environment

*pip install django* :|Django framework

*pip install djangorestframework* : |our rest framework

*python manage.py runserver* :|Start our server


# structure
the APIs are accesse by the link http://127.0.0.1:8000/api
this produces the api structure for {task create,list,delet,edit}

The front end is accessed on  http://127.0.0.1:8000/
 this redirects the user to a login page or register page if not registered
 
we have to start the server with the following command
 python manage.py runserver

# working
The front end always acceses the database via the api 

