from rest_framework import serializers

from post.models import Post

class PostSerializer(serializers.ModelSerializer):
	class Meta:
		model = Post
		fields = ('id', 'user', 'title', 'content', 'like', 'tags', 'is_archive', 'date', 'updated')
