from django.urls import path
from .views import *

urlpatterns = [
	path('', index, name='home'),
	path('feed/', feed, name='feed'),
	path('network/', network, name='network'),
	path('jobs/', jobs, name='jobs'),
	path('chat/', chat, name='chat'),
	path('notices/', notices, name='notices'),
]