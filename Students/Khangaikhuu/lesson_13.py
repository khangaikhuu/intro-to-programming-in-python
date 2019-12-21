# Allowing Users to Own Their Data
# Users should be able to enter data exclusive to them, so we’ll create a system
# to figure out which data belongs to which user. Then we’ll restrict access to
# certain pages so users can work with only their own data.

# We’ll modify the Topic model so every topic belongs to a specific user.
# This will also take care of entries, because every entry belongs to a specific
# topic. We’ll start by restricting access to certain pages.

# Restricting Access with @login_required
# Restricting Access to the Topics Page
# Each topic will be owned by a user, so only registered users can request the
# topics page. Add the following code to learning_logs/views.py:

from django.contrib.auth.decorators import login_required


@login_required
def topics(request):
    """Show all topics."""

# To make this redirect work, we need to modify settings.py so Django
# knows where to find the login page. Add the following at the very end of
# settings.py:

# My settings
LOGIN_URL = 'users:login'


# Restricting Access Throughout Learning Log
# Django makes it easy to restrict access to pages, but you have to decide
# which pages to protect. It’s best to think about which pages need to be
# unrestricted first, and then restrict all the other pages in the project.
# Here’s learning_logs/views.py with @login_required decorators applied to
# every view except index() :

# Connecting Data to Certain Users

# Next, we need to connect the data to the user who submitted it. We need to
# connect only the data highest in the hierarchy to a user, and the lower-level
# data will follow. For example, in Learning Log, topics are the highest level
# of data in the app, and all entries are connected to a topic. As long as each
# topic belongs to a specific user, we can trace the ownership of each entry in
# the database.

# Modifying the Topic Model
# The modification to models.py is just two lines:

# in models.py
from django.contrib.auth.models import User

owner = models.ForeignKey(User, on_delete=models.CASCADE)


# Identifying Existing Users
# When we migrate the database, Django will modify the database so it can
# store a connection between each topic and a user. To make the migration,
# Django needs to know which user to associate with each existing topic.

python manage.py shell
>>> from django.contrib.auth.models import User
>>> User.objects.all()
>>> for user in User.objects.all():
    ...
print(user.username, user.id)
...
ll_admin 1
eric 2
willie 3


# Migrating the Database
# Now that we know the IDs, we can migrate the database. When we do this,
# Python will ask us to connect the Topic model to a particular owner tempo-
# rarily or to add a default to our models.py file to tell it what to do. Choose
# option 1:

(ll_env)django_project$ python manage.py makemigrations learning_logs

You are trying to add a non-nullable field 'owner' to topic without a default;
we can't do that (the database needs something to populate existing rows).
Please select a fix:
1) Provide a one-off default now (will be set on all existing rows with a
    null value for this column)
2) Quit, and let me add a default in models.py
Select an option: 1
Please enter the default value now, as valid Python
The datetime and django.utils.timezone modules are available, so you can do
e.g. timezone.now
Type 'exit' to exit this prompt
                         >>> 1
Migrations for 'learning_logs':
    learning_logs/migrations/0003_topic_owner.py
                                 - Add field owner to topic

    (ll_env)django_project$ python manage.py migrate

    # We can verify that the migration worked as expected in the shell session, like this:
    >>> from learning_logs.models import Topic
    >>> for topic in Topic.objects.all():
        ...
    print(topic, topic.owner)
        ...
        ...

    # Restricting Topics Access to Appropriate Users
    # Currently, if you’re logged in, you’ll be able to see all the topics, no matter
    # which user you’re logged in as. We’ll change that by showing users only the
    # topics that belong to them.
    # Make the following change to the topics() function in views.py:

    topics = Topic.objects.filter(owner=request.user).order_by('date_added')

    # Protecting a User’s Topics
    # adding in views.py the following

    from django.http import Http404

    # add the following code into the topic function of views.py
    # Make sure the topic belongs to the current user.

    if topic.owner != request.user:
        raise Http404


    # Protecting the edit_entry Page
    # http://localhost:8000/edit_entry/entry_id/
    if topic.owner != request.user:
        raise Http404

    # Associating New Topics with the Current User
    # Add the following code,
    # which associates the new topic with the current user:
    new_topic = form.save(commit=False)
    new_topic.owner = request.user
    new_topic.save()

    return redirect('learning_logs:topics')

# S t y l ing a nd De ploy ing a n A pp
# Learning Log is fully functional now, but it
# has no styling and runs only on your local
# machine. In this chapter, you’ll style the pro­
# ject in a simple but professional manner and
# then deploy it to a live server so anyone in the world
# can make an account and use it.

(ll_env)django_project$ pip install django-bootstrap4

# Next, we need to add the following code to include django-bootstrap4
# in INSTALLED_APPS in settings.py:

# Using Bootstrap to Style Learning Log
# Modifying base.html
# We need to modify the base.html template to accommodate the Bootstrap
# template. I’ll introduce the new base.html in parts.
# Defining the HTML Headers

{% load bootstrap4 %}
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1,
shrink-to-fit=no">
 <title>Learning Log</title>

{% bootstrap_css %}
{% bootstrap_javascript jquery='full' %}
 </head>

# Defining the Navigation Bar
<body>

<nav class="navbar navbar-expand-md navbar-light bg-light mb-4 border">
 <a class="navbar-brand" href="{% url 'learning_logs:index'%}">Learning Log</a>
 <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarCollapse"
aria-controls="navbarCollapse" aria-expanded="false" aria-label="Toggle navigation">
<span class="navbar-toggler-icon"></span></button>
<div class="collapse navbar-collapse" id="navbarCollapse">
<ul class="navbar-nav mr-auto">
<li class="nav-item">
<a class="nav-link" href="{% url 'learning_logs:topics'%}">
Topics</a></li>
</ul>
<ul class="navbar-nav ml-auto">
{% if user.is_authenticated %}
<li class="nav-item">
<span class="navbar-text"}">Hello, {{ user.username }}.</span>
</li>
<li class="nav-item">
<a class="nav-link" href="{% url 'users:logout' %}">Log out</a>
</li>
{% else %}
<li class="nav-item">
<a class="nav-link" href="{% url 'users:register' %}">Register</a>
</li>
<li class="nav-item">
<a class="nav-link" href="{% url 'users:login' %}">Log in</a></li>
{% endif %}
</ul>
</div>
</nav>

# Defining the Main Part of the Page
<main role="main" class="container">
<div class="pb-2 mb-2 border-bottom">
{% block page_header %}{% endblock page_header %}
</div>
<div>
{% block content %}{% endblock content %}
</div>
</main>
</body>
</html>


# Styling the Home Page Using a Jumbotron
# To update the home page, we’ll use a Bootstrap element called a jumbotron,
# which is a large box that stands out from the rest of the page and can con-
# tain anything you want. Typically, it’s used on home pages to hold a brief
# description of the overall project and a call to action that invites the viewer
# to get involved.
# Here’s the revised index.html file:

{% extends "learning_logs/base.html" %}
{% block page_header %}

<div class="jumbotron">

<h1 class="display-3">Track your learning.</h1>

<p class="lead">Make your own Learning Log, and keep a list of the
topics you're learning about. Whenever you learn something new
about a topic, make an entry summarizing what you've learned.</p>
<a class="btn btn-lg btn-primary" href="{% url 'users:register' %}"
role="button">Register &raquo;</a>
</div>
 {% endblock page_header %}


# Styling the Login Page
# We’ve refined the overall appearance of the login page but not the login
# form yet. Let’s make the form look consistent with the rest of the page by
# modifying the login.html file:

{% extends "learning_logs/base.html" %}
 {% load bootstrap4 %}
 {% block page_header %}
<h2>Log in to your account.</h2>
{% endblock page_header %}
{% block content %}
<form method="post" action="{% url 'users:login' %}" class="form">
{% csrf_token %}

{% bootstrap_form form %}

{% buttons %}
<button name="submit" class="btn btn-primary">Log in</button>
{% endbuttons %}

<input type="hidden" name="next"
value="{% url 'learning_logs:index' %}" />
</form>
{% endblock content %}

# Styling the Topics Page
# Let’s make sure the pages for viewing information are styled appropriately
# as well, starting with the topics page:

{% extends "learning_logs/base.html" %}
{% block page_header %}
<h1>Topics</h1>
{% endblock page_header %}
{% block content %}
<ul>
{% for topic in topics %}

<li><h3>
<a href="{% url 'learning_logs:topic' topic.id %}">{{ topic }}</a>
</h3></li>
{% empty %}
<li><h3>No topics have been added yet.</h3></li>
{% endfor %}
</ul>

<h3><a href="{% url 'learning_logs:new_topic' %}">Add a new topic</a></h3>
{% endblock content %}


# Styling the Entries on the Topic Page
# The topic page has more content than most pages, so it needs a bit more
# work. We’ll use Bootstrap’s card component to make each entry stand out.
# A card is a div with a set of flexible, predefined styles that’s perfect for dis­
# playing a topic’s entries: Add in topic.html

{% extends 'learning_logs/base.html' %}
 {% block page_header %}
<h3>{{ topic }}</h3>
{% endblock page_header %}
{% block content %}
<p>
<a href="{% url 'learning_logs:new_entry' topic.id %}">Add new entry</a>
</p>
{% for entry in entries %}
<div class="card mb-3">
<h4 class="card-header">
{{ entry.date_added|date:'M d, Y H:i' }}
<small><a href="{% url 'learning_logs:edit_entry' entry.id %}">
edit entry</a></small>
</h4>
<div class="card-body">
{{ entry.text|linebreaks }}
</div>
</div>
{% empty %}
<p>There are no entries for this topic yet.</p>
{% endfor %}
{% endblock content %}



# pushing to the heroku and run it on heroku
#

# Installing the Heroku CLI
#https://devcenter.heroku.com/articles/heroku-cli/

    # Installing Required Packages
    (ll_env)django_project$ pip install psycopg2==2.7.*
    (ll_env)django_project$ pip install django-heroku
    (ll_env)django_project$ pip install gunicorn

    # psycopg2 is used to manage database that heroku uses
    # django-heroku package handles almost the entire configuration our app needs to run property on heroku server
    # the gunicorn provides a server capable of serving apps in a live environment


    # Creating a requirements.txt File
    # Heroku needs to know which packages our project depends on, so we’ll use
    # pip to generate a file listing them. Again, from an active virtual environment, issue the following command:
    (ll_env)django_project$ pip freeze > requirements.txt

    dj-database-url==0.5.0
    Django==2.2.0
    django-bootstrap4==0.0.7
    django-heroku==0.3.1
    gunicorn==19.9.0
    psycopg2==2.7.7
    pytz==2018.9
    sqlparse==0.2.4
    whitenoise==4.1.2

    # Specifying the Python Runtime
    (ll_env)django_project$ python --version

    # Make a new file called runtime.txt in the same directory as manage.py, and enter the following:
    python-3.7.5

    # If you get an error reporting that the Python runtime you requested isn’t available, go
    # to https://devcenter.heroku.com/categories/language-support/ and look for
    # a link to Specifying a Python Runtime. Scan through the article to find the avail-
    # able runtimes, and use the one that most closely matches your Python version.

    # Modifying settings.py for Heroku
    # Now we need to add a section at the end of settings.py to define some specific
    # settings for the Heroku environment:

    # Heroku settings.
    import django_heroku
    django_heroku.settings(locals())

    # Making a Procfile to Start Processes
    # A Procfile tells Heroku which processes to start to properly serve the project.
    #     Save this one-line file as Procfile, with an uppercase P and no file extension,
    # in the same directory as manage.py.
    web: gunicorn learn_log.wsgi --log-file -

    # This line tells Heroku to use gunicorn as a server and to use the set­
    # tings in learn_log/wsgi.py to launch the app. The log-file flag tells
    # Heroku the kinds of events to log.

    git add .
    git commit -m "Ready to push to the Heroku"

    # after you installed heroku cli you will be able to run
    heroku login

    heroku create

    git push heroku master

    heroku ps

    heroku open

    # Setting Up the Database on Heroku
    # We need to run migrate once to set up the live database and apply all the
    # migrations we generated during development. You can run Django and
    # Python commands on a Heroku project using the command heroku run .
    # Here’s how to run migrate on the Heroku deployment:
    heroku run python manage.py migrate

    (ll_env)django_project$ heroku open
