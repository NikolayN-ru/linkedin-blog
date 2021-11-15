from django.contrib import admin
from .models import *

admin.site.register(Tag)
admin.site.register(Article)
admin.site.register(Group)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
	list_display = ('user', 'title', 'like', 'image', 'is_archive', 'date')
	list_filter = ('date', 'like', 'updated')
	search_fields = ('title', 'slug', 'content')
	prepopulated_fields = {'slug':('title',)}
	ordering = ('is_archive', 'date')

# admin.site.register(Post)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
	list_display = ('user', 'post', 'title')
	list_filter = ('user',)
	search_fields = ('title',)

# admin.site.register(Comment)
