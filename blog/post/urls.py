from django.urls import path
from .views import *

# app_name = 'post'

urlpatterns = [
	path('', index, name='home'),
	path('feed/', FeedView.as_view(), name='feed'),
	# path('feed/', feed, name='feed'),
	path('network/', network, name='network'),
	path('jobs/', jobs, name='jobs'),
	path('chat/', chat, name='chat'),
	path('notices/', notices, name='notices'),
	path('post/<int:id>/', post, name='post'),
]