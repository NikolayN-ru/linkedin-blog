from rest_framework import generics, permissions

from post.models import Post
from .permissions import IsAuthorOrReadOnly
from .serializers import PostSerializer

class PostAPIView(generics.ListCreateAPIView):
	# permission_classes = (permissions.IsAuthenticated,)
	queryset = Post.objects.all()
	serializer_class = PostSerializer

class PostAPIViewDetail(generics.RetrieveUpdateDestroyAPIView):
	permission_classes = (IsAuthorOrReadOnly,)
	queryset = Post.objects.all()
	serializer_class = PostSerializer
