from django.shortcuts import render
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView

# Create your views here.
def index(request):
	return render(request, 'index.html', {})

class FeedView(ListView):
	queryset = Post.published.all()
	context_object_name = 'posts'
	paginate_by = 2
	template_name = 'feed.html'

# def feed(request):
# 	posts = Post.published.all()
# 	paginator = Paginator(posts, 2)
# 	page = request.GET.get('page')
# 	try:
# 		posts = paginator.page(page)
# 	except PageNotAnInteger:
# 		posts = paginator.page(1)
# 	except EmptyPage:
# 		posts = paginator.page(paginator.num_pages)
# 	return render(request, 'feed.html', {'page': page, 'posts':posts})

def network(request):
	return render(request, 'network.html', {})

def jobs(request):
	return render(request, 'jobs.html', {})

def chat(request):
	return render(request, 'chat.html', {})

def notices(request):
	return render(request, 'notices.html', {})

def post(request, id):
	post = Post.objects.get(pk = id)
	return render(request, 'post.html', {'post':post})
