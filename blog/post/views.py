from django.shortcuts import render
from .models import Post, Comment
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from .forms import EmailPostForm, CommentForm
from django.core.mail import send_mail
from django.contrib import messages

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
	comments = post.comments.all()
	new_comment = None
	if request.method == 'POST':
		comment_form = CommentForm(data=request.POST)
		if comment_form.is_valid():
			new_comment = comment_form.save(commit=False)
			new_comment.post = post
			new_comment.save()
	else:
		comment_form = CommentForm()
	return render(request, 'post.html', {'post':post,
	'comments': comments,
	'new_comment': new_comment,
	'comment_form':comment_form})




def post_share(request, post_id):
	post = Post.objects.get(pk = post_id)
	sent = False
	if request.method == 'POST':
		form = EmailPostForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			post_url = request.build_absolute_uri(post.get_absolute_url())
			subject = '{}({}) recommends you reading "{}" '.format(cd['name'], cd['email'], post.title)
			message = 'Read "{}" at {}\n\n{}\'s comments: {}'.format(post.title, post_url, cd['name'], cd['comments'])
			send_mail(subject, message, 'admin@myblog.com', [cd['to']])
			sent = True
	else:
		messages.success(request, 'форма валидна-заполняйте')
		form = EmailPostForm()
	return render(request, 'network.html', {'post': post, 'form': form, 'sent': sent})
