# Setting Up User Accounts
# 2019/12/19
# In this section, we’ll set up a user registration and authorization system so
# people can register an account and log in and out.

# We’ll create a new app
# to contain all the functionality related to working with users. We’ll use the
# default user authentication system included with Django to do as much
# of the work as possible. We’ll also modify the Topic model slightly so every
# topic belongs to a certain user

# write down the following command in learn_log folder

python manage.py startapp users

# it will create a folder with the name users
# Adding users to settings.py in INSTALLED_APPS
'users',

# Including the URLs from users
# In urls.py we need to add urls.py in urlpatterns
path('users/', include('users.urls')),

# The Login Page
# We’ll first implement a login page. We’ll use the default login view Django
# provides, so the URL pattern for this app looks a little different. Make a new
# urls.py file in the directory learn_log/users/, and add the following to it:

"""Defines URL patterns for users"""
from django.urls import path, include

app_name = 'users'
urlpatterns = [
    # Include default auth urls.
    path('', include('django.contrib.auth.urls')),
]

# The login Template
# When the user requests the login page, Django will use a default view
# function, but we still need to provide a template for the page.
# Inside the learn_log/users/ directory, make
# a directory called templates; inside that, make another directory 
# called registration. Here’s the login.html template, which you 
# should save in learn_log/users/templates/registration:

{% extends "learning_logs/base.html" %}
{% block content %}
 {% if form.errors %}
    <p>Your username and password didn't match. Please try again.</p>
 {% endif %}
    <form method="post" action="{% url 'users:login' %}">
    {% csrf_token %}
        {{ form.as_p }}

        <button name="submit">Log in</button>
        <input type="hidden" name="next"
        value="{% url 'learning_logs:index' %}" />
    </form>
{% endblock content %}


# Linking to the Login Page
# Let’s add the login link to base.html so it appears on every page. We don’t
# want the link to display when the user is already logged in, so we nest it
# inside an {% if %} tag:
{% if user.is_authenticated %}
    Hello, {{ user.username }}.
{% else %}
    <a href="{% url 'users:login' %}">Log in</a>
{% endif %}


# Logging Out
# Now we need to provide a way for users to log out. We’ll put a link in base
# .html that logs out users; when they click this link, they’ll go to a page con-
# firming that they’ve been logged out.


# Adding a Logout Link to base.html
# We’ll add the link for logging out to base.html so it’s available on every
# page. We’ll include it in the {% if user.is_authenticated %} portion so only
# users who are already logged in can see it:

# The Logout Confirmation Page
# Users will want to know that they’ve successfully logged out, so the default log-
# out view renders the page using the template logged_out.html, which we’ll cre-
# ate now.
# put into logged_out.html

{% extends "learning_logs/base.html" %}
{% block content %}
<p>You have been logged out. Thank you for visiting!</p>
{% endblock content %}

# The Registration Page
# Next, we’ll build a page so new users can register. We’ll use Django’s default
# 
UserCreationForm 
# 
# but write our own view function and template.

# The register URL

# The register URL
# The following code provides the URL pattern for the registration page,
# again in users/urls.py:

from . import views
# Registration page.
path('register/', views.register, name='register'),


from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
# The register() View Function
def register(request):
    """Register a new user."""  
    if request.method != 'POST':
    # Display blank registration form.
        form = UserCreationForm()
    else:
    # Process completed form.
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            # Log the user in and then redirect to home page.y

            login(request, new_user)
            return redirect('learning_logs:index')

    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'registration/register.html', context)


# the register template
{% extends "learning_logs/base.html" %}
{% block content %}
    <form method="post" action="{% url 'users:register' %}">
        {% csrf_token %}
        {{ form.as_p }}
        <button name="submit">Register</button>
        <input type="hidden" name="next" value="{% url 'learning_logs:index' %}" />
    </form>
{% endblock content %}

# Linking to the Registration Page
# Next, we’ll add the code to show the registration page link to any user who
# isn’t currently logged in
<a href="{% url 'users:register' %}">Register</a> -


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
<QuerySet [<User: ll_admin>, <User: eric>, <User: willie>]>
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

(ll_env)learning_log$ python manage.py makemigrations learning_logs
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
(ll_env)learning_log$


# pushing to the heroku and run it on heroku
# 1. Install heroku on your computer
# 2. login to heroku on console
# 3. create Procfile in a root folder
# 4. add 
#     ---web: gunicorn intro-to-programming-in-python.wsgi --log-file -
# 5. runtime.txtAdd a runtime.txt file in the project root directory and specify the correct Python version
# 6. python-3.7.5
# 7. pip install gunicorn dj-database-url whitenoise psycopg2
# 8. pip freeze > requirements.txt
# 9. echo "python-3.7.5" >> runtime.txt
# 10. echo "web: gunicorn <your_project_name>.wsgi" >> Procfile