from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, 'index.html', {})

def feed(request):
	return render(request, 'feed.html', {})

def network(request):
	return render(request, 'network.html', {})

def jobs(request):
	return render(request, 'jobs.html', {})

def chat(request):
	return render(request, 'chat.html', {})

def notices(request):
	return render(request, 'notices.html', {})