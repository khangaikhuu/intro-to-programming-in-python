# 11
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
# ence is the addition of a new module called 
# forms.py, which will contain
# the forms.

# 
# The Topic ModelForm

# The simplest way to build a form in Django is to use a ModelForm, which
# uses the information from the models we defined to auto-
# matically build a form. Write your first form in the file 
forms.py
# which you
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
# wants to add a new topic, we’ll send them to 
http://localhost:8000/new_topic/
# Here’s the URL pattern for the new_topic page, which you add to 
# learning_logs/urls.py:

# Page for adding a new topic
path('new_topic/', views.new_topic, name='new_topic'),

# The new_topic() function needs to handle two different situations: initial
# requests for the new_topic page (in which case it should show a blank form)
# and the processing of any data submitted in the form. After data from a
# submitted form is processed, it needs to redirect the user back to the topics
# page: 
# add the following code into views.py
from django.shortcuts import render, redirect


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

# The two main types of request you’ll use when building web apps are GET
# requests and POST requests. You use GET requests for pages that only read
# data from the server.


# The new_topic Template
# Now we’ll make a new template called new_topic.html to display the form we
# just created.
{% extends "learning_logs/base.html" %}
{% block content %}
    <p>Add a new topic:</p>

    <form action="{% url 'learning_logs:new_topic' %}" method='post'>
        {% csrf_token %}
        {{ form.as_p }}
        <button name="submit">Add topic</button>
    </form>
{% endblock content %}

# Django uses the template tag {% csrf_token %} to prevent attackers
# from using the form to gain unauthorized access to the server (this kind
# of attack is called a cross-site request forgery).

# Linking to the new_topic Page
# Next, we include a link to the new_topic page on the topics page:
<a href="{% url 'learning_logs:new_topic' %}">Add a new topic</a>


# 11.2 Adding New Entries
# add the following into forms.py

from .models import Topic, Entry

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': 'Entry:'}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}

# A widget is an HTML form ele-
# ment, such as a single-line text box, multi-line text area, or drop-down list.

# The new_entry URL
# add the following into learning_logs/urls.py

# Page for adding a new entry
path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),

# The new_entry() View Function
# Add the following code to your views.py file:
from .forms import TopicForm, EntryForm
def new_entry(request, topic_id):
    """Add a new entry for a particular topic."""
    topic = Topic.objects.get(id=topic_id)
    
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = EntryForm()
    else:
        # POST data submitted; process data.
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('learning_logs:topic', topic_id=topic_id)
    # Display a blank or invalid form.
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)

# The new_entry Template
# create new_entry.html in template folder and add the following template file
{% extends "learning_logs/base.html" %}
{% block content %}

    <p><a href="{% url 'learning_logs:topic' topic.id %}">{{ topic }}</a></p>
    <p>Add a new entry:</p>
    <form action="{% url 'learning_logs:new_entry' topic.id %}" method='post'>
        {% csrf_token %}
        {{ form.as_p }}
        <button name='submit'>Add entry</button>
    </form>
{% endblock content %}

# Linking to the new_entry Page
# add the following lines of code into topic.html
<p>Entries:</p>
<p>
<a href="{% url 'learning_logs:new_entry' topic.id %}">Add new entry</a>
</p>
<ul>


# 11.3 
# Editing Entries
# The edit_entry URL

# learning_logs/urls.py:
# Page for editing an entry.
path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),

# The edit_entry() View Function
# add into views.py
from .models import Topic, Entry

def edit_entry(request, entry_id):
    """Edit an existing entry."""

    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic

    if request.method != 'POST':
        # Initial request; pre-fill form with the current entry.
        form = EntryForm(instance=entry)
    else:
        # POST data submitted; process data.
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic', topic_id=topic.id)
    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)

# The edit_entry Template
# add the following into edit_entry.html
{% extends "learning_logs/base.html" %}
{% block content %}
    <p><a href="{% url 'learning_logs:topic' topic.id %}">{{ topic }}</a></p>
    <p>Edit entry:</p>

    <form action="{% url 'learning_logs:edit_entry' entry.id %}" method='post'>
        {% csrf_token %}
        {{ form.as_p }}
        <button name="submit">Save changes</button>
    </form>
{% endblock content %}

# Linking to the edit_entry Page
# edit_entry page for each entry on the topic page
# add the following into topic.html
<p>{{ entry.text|linebreaks }}</p>
<p>
        <a href="{% url 'learning_logs:edit_entry' entry.id %}">Edit entry</a>
</p>