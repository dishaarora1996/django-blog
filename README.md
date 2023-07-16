# Introduction

This django project is a portal for users to create blog posts and shows the list of blog posts uploaded to this website by users. Users need to login to create, update, and delete their respective blog posts.


## Setup
The first thing to do is to clone the repository:

$ git clone https://github.com/dishaarora1996/django-blog.git
$ cd django-blog

### Activate the virtualenv for your project.

Create a virtual environment to install dependencies in and activate it:

$ python -m venv env
$ source env/bin/activate

### Install the dependencies:

(env)$ pip install -r requirements.txt

### Then simply apply the migrations:

$ python manage.py migrate

### Now run the development server:

Once pip has finished downloading the dependencies:

(env)$ python manage.py runserver
And navigate to http://127.0.0.1:8000/
