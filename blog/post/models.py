from django.db import models
from django.contrib.auth.models import User

class Comment(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
	title = models.CharField(max_length=255, verbose_name='заголовок')
	content = models.TextField(blank=True, verbose_name='тело поста')

class Tag(models.Model):
	title = models.CharField(max_length=255, blank=True, null=True, verbose_name='имя тега')
	name = models.ManyToManyField('Post', blank=True, null=True, related_name='related_post')

class Post(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
	title = models.CharField(max_length=255, verbose_name='заголовок')
	slug = models.SlugField(max_length=255, unique_for_date='date')
	content = models.TextField(blank=True, verbose_name='тело поста')
	like = models.PositiveIntegerField(default=0, verbose_name='количество лайков')
	comment = models.ForeignKey(Comment, on_delete=models.CASCADE, blank=True, null=True, verbose_name='коментарии')
	filefield = models.FileField( blank=True, null=True, verbose_name='файл')
	image = models.ImageField(blank=True, null=True, verbose_name='изображение')
	tags = models.ManyToManyField(Tag, blank=True, null=True, related_name='related_tags')
	is_archive = models.BooleanField(default=False, null=True, verbose_name='в архиве')
	date = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title


class Article(models.Model):
	name = models.CharField(max_length=255, verbose_name='заголовок')
	description = models.TextField(blank=True, verbose_name='тело статьи')
	
class Group(models.Model):
	name = models.CharField(max_length=255, verbose_name='имя группы')
	article = models.ForeignKey(Article, on_delete=models.CASCADE, blank=True, null=True, verbose_name='статьи')

