from django.urls import path
from . import views
app_name = 'learning_logs'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Topics page
    path('topics/', views.topics, name='topics'),
    # Topic page
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    # topics/1/ - Path parameter
    # topics?id=1 - Query parameter
]

