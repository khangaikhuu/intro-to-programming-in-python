# Project Web application
# Django - Project Learning Log
# An online journal system that lets you keep
# track of information you’ve learned about particular
# topics.

# 1. Specification
# We’ll write a web app called Learning Log that allows users to
# log the topics they’re interested in and to make journal entries as
# they learn about each topic. The Learning Log home page will
# describe the site and invite users to either register or log in. Once
# logged in, a user can create new topics, add new entries, and read
# and edit existing entries.

# 1. Setting Up a project
# After you installed virtual env
# Creating your virtual environment in your own folder
python -m venv ll_env

# Activating virtual environment 
source ll_env/bin/activate

# For deactivating 
deactivate

# Installing django using PIP
pip install django

# Create new learn_log project using django-admin
django-admin startproject learn_log .

# Creating the Database
python manage.py migrate

# Viewing the Project
python manage.py runserver


"""
Ex.9.1
New Projects: To get a better idea of what Django does, build a couple
of empty projects and look at what Django creates. Make a new folder with a
simple name, like snap_gram or insta_chat (outside of your learning_log direc-
tory), navigate to that folder in a terminal, and create a virtual environment.
Install Django and run the command django-admin.py startproject snap_gram .
(make sure you include the dot at the end of the command).
Look at the files and folders this command creates, and compare them to
Learning Log. Do this a few times until you’re familiar with what Django creates
when starting a new project. Then delete the project directories if you wish.
"""

# Starting an App
python manage.py startapp learning_logs

# The command startapp appname tells Django to create the infrastructure
# needed to build an app.

# Defining Models
# Creating topic model for the application
class Topic(models.Model):
    """A topic the user is learning about."""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of the model."""
        return self.text

# Add our app to this list by modifying INSTALLED_APPS so it looks like this:
# INSTALLED_APPS = [
#       My apps
#       'learning_logs',
#       Default django apps.

# Activating Models
python manage.py makemigrations learning_logs

# migrating database
python manage.py migrate

# 9.2 The Django Admin Site

# Django makes it easy to work with your models through the admin site. Only
# the site’s administrators use the admin site, not general users. In this sec-
# tion, we’ll set up the admin site and use it to add some topics through the
# Topic model.

# Setting Up a Superuser
# Django allows you to create a superuser, a user who has all privileges avail-
# able on the site.

python manage.py createsuperuser

# then give a super username and password
# give the a password which can may secure

# Registering a Model with the Admin Site
# open the admin.py file

from .models import Topic

admin.site.register(Topic)

# RUN python manage.py runserver

# Adding Topic - Rock Climbing  and Chess
# Defining the Entry Model

# For a user to record what they’ve been learning about chess and rock climb-
# ing, we need to define a model for the kinds of entries users can make in
# their learning logs. Each entry needs to be associated with a particular
# topic. This relationship is called a "many-to-one" relationship, meaning many
# entries can be associated with one topic.
# Here’s the code for the Entry model. Place it in your models.py file:

class Entry(models.Model):
    """Something specific learned about a topic."""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

class Meta:
    verbose_name_plural = 'entries'
    def __str__(self):
        """Return a string representation of the model."""
        return f"{self.text[:50]}..."


# Migrating the Entry Model again
python manage.py makemigrations learning_logs

# Then run 
python manage.py migrate

# Registering Entry with the Admin Site
admin.site.register(Entry)

# run the application 
python manage.py runserver

# then add some entries for the topics Rock Climbing and Chess


# 9.3 The Django Shell

# using python manage.py shell command to enter directly to the application

from learning_logs.models import Topic
Topic.objects.all()

topics = Topic.objects.all()
for topic in topics:
    print(topic.id, topic)

t = Topic.objects.get(id=1)
t.text
t.date_added

t.entry_set.all()

"""
Ex.9.2 
Short Entries: The __str__() method in the Entry model currently appends
an ellipsis to every instance of Entry when Django shows it in the admin site
or the shell. Add an if statement to the __str__() method that adds an ellipsis
only if the entry is longer than 50 characters. Use the admin site to add an
entry that’s fewer than 50 characters in length, and check that it doesn’t have
an ellipsis when viewed.
Ex.9.3 
The Django API: When you write code to access the data in your project,
you’re writing a query. Skim through the documentation for querying your data
at https://docs.djangoproject.com/en/3.0/topics/db/queries/. Much of what
you see will look new to you, but it will be very useful as you start to work on
your own projects.

Ex.9.4 
Pizzeria: Start a new project called pizzeria with an app called pizzas .
Define a model Pizza with a field called name , which will hold name values,
such as Hawaiian and Meat Lovers . Define a model called Topping with fields
called pizza and name . The pizza field should be a foreign key to Pizza , and
name should be able to hold values such as pineapple , Canadian bacon , and
sausage .
Register both models with the admin site, and use the site to enter some
pizza names and toppings. Use the shell to explore the data you entered.
"""

# 9.4 Making Pages: The Learning Log Home Page
# Making web pages with Django consists of three stages: defining URLs,
# writing views, and writing templates. You can do these in any order, but in
# this project we’ll always start by defining the URL pattern. A URL pattern
# describes the way the URL is laid out. It also tells Django what to look for
# when matching a browser request with a site URL so it knows which page to
# return.

# In the main learn_log project folder, open the file urls.py.
# Add
from django.urls import path, include

# Then add 
path('', include('learning_logs.urls')),

# Now Create a new Python file and save it as urls.py in learning_logs,

# Add the following content
"""Defines URL patterns for learning_logs."""
from django.urls import path
from . import views
app_name = 'learning_logs'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
]

# We also import the views module; the
# dot tells Python to import the views.py

# Writing a View

# Open views.py file and add 
def index(request):
    """The home page for Learning Log."""
    return render(request, 'learning_logs/index.html')

# After saved your views.py file the contents, then run the app
# calling python manage.py runserver
# refresh your webbrowser using the url http://127.0.0.1:8000


# Writing a Template

# The template defines what the page should look like, and Django fills in
# the relevant data each time the page is requested.
# Inside the learning_logs folder, make a new folder called templates. Inside
# the templates folder, make another folder called learning_logs. This might seem
# a little redundant (we have a folder named learning_logs inside a folder named
# templates inside a folder named learning_logs), but it sets up a structure that
# Django can interpret unambiguously, even in the context of a large project
# containing many individual apps. Inside the inner learning_logs folder, make
# a new file called index.html. The path to the file will be 
# learning_logs/templates/learning_logs/index.html. Enter the following code into that file:

<p>Learning Log</p>
<p>Learning Log helps you keep track of your learning, for any topic you're
learning about.</p>

# By running python manage.py runserver, you will see simple web application
# written in python

