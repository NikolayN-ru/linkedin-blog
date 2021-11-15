from django.urls import path
from .views import PostAPIView, PostAPIViewDetail

urlpatterns = [
	path('<int:pk>/', PostAPIViewDetail.as_view()),
	path('', PostAPIView.as_view()),
]
