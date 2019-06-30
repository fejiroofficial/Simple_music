# Music Service API
## About
This is a simple music service API for learning the Django REST Framework.
## Goal
The goal of this project is to get my hands on wet on Django REST framework.
## Features
With this API;
- You can create, view, update, and delete a song
## Technology stack
Tools used during the development of this API are;
- [Django](https://www.djangoproject.com) - a python web framework
- [Django REST Framework](http://www.django-rest-framework.org) - a flexible toolkit to build web APIs
- [Postgresql](https://www.postgresql.org/) - this is a database server
## Requirements
- Use Python 3.x.x+
- Use Django 2.x.x+
## Tests
```sh 
    $ python manage.py test
```
## Running the application
To run this application, clone the repository on your local machine and execute the following command.
```sh
    $ cd music_service
    $ virtualenv virtenv
    $ source virtenv/bin/activate
    $ pip install -r requirements.txt
    $ python manage.py makemigrations
    $ python manage.py migrate
    $ python manage.py runserver
```
