from django.contrib import admin
from .models import *

admin.site.register(Comment)
admin.site.register(Tag)
admin.site.register(Post)
admin.site.register(Article)
admin.site.register(Group)