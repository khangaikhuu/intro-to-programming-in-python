
# Building Additional Pages

# Now that we’ve established a routine for building a page, we can start to
# build out the Learning Log project. We’ll build two pages that display data:
# a page that lists all topics and a page that shows all the entries for a particu-
# lar topic. For each page, we’ll specify a URL pattern, write a view function,
# and write a template. But before we do this, we’ll create a base template
# that all templates in the project can inherit from.

# Template Inheritance

# 
# The Parent Template
# We’ll create a template called base.html in the same directory as index.html.
# This file will contain elements common to all pages; every other template
# will inherit from base.html. The only element we want to repeat on each
# page right now is the title at the top. Because we’ll include this template on
# every page, let’s make the title a link to the home page:

# We’ll create a template called base.html in the same directory as index.html.
# This file will contain elements common to all pages; every other template
# will inherit from base.html. The only element we want to repeat on each
# page right now is the title at the top. Because we’ll include this template on
# every page, let’s make the title a link to the home page:
# base.html

<p>
<a href="{% url 'learning_logs:index' %}">Learning Log</a>
</p>
{% block content %}{% endblock content %}

# The Child Template
# Now we need to rewrite index.html to inherit from base.html. Add the follow-
# ing code to index.html:
{% extends "learning_logs/base.html" %}
{% block content %}
{% endblock content %}

# In a large project, it’s common to have one parent template called base.html for
# the entire site and parent templates for each major section of the site. All the section
# templates inherit from base.html, and each page in the site inherits from a section
# template. This way you can easily modify the look and feel of the site as a whole, any
# section in the site, or any individual page. This configuration provides a very effi-
# cient way to work, and it encourages you to steadily update your site over time.

# The Topics Page

# The Topics URL Pattern
# First, we define the URL for the topics page. It’s common to choose a ­simple
# URL fragment that reflects the kind of information presented on the page.

# We’ll use the word topics, so the URL http://localhost:8000/topics/ will return
# this page.

# add to urls.py
path('topics/', views.topics, name='topics'),


# add the following code to views.py
from .models import Topic
def topics(request):
    """Show all topics."""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

# create new topics.html file beside index.html then add the following
{% extends "learning_logs/base.html" %}
{% block content %}
<p>Topics</p>
<ul>
    {% for topic in topics %}
        <li>{{ topic }}</li>
    {% empty %}
        <li>No topics have been added yet.</li>
    {% endfor %}
</ul>
{% endblock content %}

# add following in base.html
<p>
    <a href="{% url 'learning_logs:index' %}">Learning Log</a>
    <a href="{% url 'learning_logs:topics' %}">Topics</a>
</p>

# Individual Topic Pages
# Next, we need to create a page that can focus on a single topic, showing the
# topic name and all the entries for that topic. We’ll again define a new URL
# pattern, write a view, and create a template. We’ll also modify the topics
# page so each item in the bulleted list links to its corresponding topic page.

# The Topic URL Pattern
# The URL pattern for the topic page is a little different than the prior URL
# patterns because it will use the topic’s id attribute to indicate which topic
# was requested. For example, if the user wants to see the detail page for the
# Chess topic, where the id is 1, the URL will be http://localhost:8000/topics/1/.

# Here’s a pattern to match this URL, which you should place in learning
# _logs/urls.py:
# Detail page for a single topic.
path('topics/<int:topic_id>/', views.topic, name='topic'),

# The Topic View
# The topic() function needs to get the topic and all associated entries from
# the database, as shown here:

def topic(request, topic_id):
    """Show a single topic and all its entries."""
    topic = Topic.objects.get(id=topic_id)

    entries = topic.entry_set.order_by('-date_added')

    context = {'topic': topic, 'entries': entries}

    return render(request, 'learning_logs/topic.html', context)

# The Topic Template
# The template needs to display the name of the topic and the entries. We
# also need to inform the user if no entries have been made yet for this topic.
# into topic.html
{% extends 'learning_logs/base.html' %}
{% block content %}

    <p>Topic: {{ topic }}</p>
    <p>Entries:</p>
    <ul>
    {% for entry in entries %}
        <li>
            <p>{{ entry.date_added|date:'M d, Y H:i' }}</p>
            <p>{{ entry.text|linebreaks }}</p>
        </li>
    {% empty %}
        <li>There are no entries for this topic yet.</li>
    {% endfor %}
    </ul>

{% endblock content %}

# Adding topic page into topics page
{% for topic in topics %}
    <li>
        <a href="{% url 'learning_logs:topic' topic.id %}">{{ topic }}</a>
    </li>
{% empty %}

# 10.2
# you’ll build forms
# so users can add their own topics and entries, and edit
# existing entries. You’ll also learn how Django guards
# against common attacks to form-based pages so you
# don’t have to spend much time thinking about secur-
# ing your apps.
# You’ll also implement a user authentication system. You’ll build a regis-
# tration page for users to create accounts, and then restrict access to certain
# pages to logged-in users only. Then you’ll modify some of the view func-
# tions so users can only see their own data. You’ll learn to keep your users’
# data safe and secure.
# Adding New Topics
# Let’s start by allowing users to add a new topic. Adding a form-based page
# works in much the same way as the pages we’ve already built: we define a
# URL, write a view function, and write a template. The one major differ-
# ence is the addition of a new module called forms.py, which will contain
# the forms.

# 
# The Topic ModelForm

# The simplest way to build a form in Django is to use a ModelForm, which
# uses the information from the models we defined to auto-
# matically build a form. Write your first form in the file forms.py, which you
# should create in the same directory as models.py:

from django import forms
from .models import Topic
class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}


# The new_topic URL
# The URL for a new page should be short and descriptive. When the user
# wants to add a new topic, we’ll send them to http://localhost:8000/new_topic/.
# Here’s the URL pattern for the new_topic page, which you add to learning
# _logs/urls.py:

# Page for adding a new topic
path('new_topic/', views.new_topic, name='new_topic'),

# The new_topic() function needs to handle two different situations: initial
# requests for the new_topic page (in which case it should show a blank form)
# and the processing of any data submitted in the form. After data from a
# submitted form is processed, it needs to redirect the user back to the topics
# page:

def new_topic(request):
    """Add a new topic."""
    if request.method != 'POST':
    # No data submitted; create a blank form.
        form = TopicForm()
    else:
    # POST data submitted; process data.
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topics')
    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)

# The new_topic Template
# Now we’ll make a new template called new_topic.html to display the form we
# just created.


# Linking to the new_topic Page
# Next, we include a link to the new_topic page on the topics page: