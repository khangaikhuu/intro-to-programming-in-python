
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

