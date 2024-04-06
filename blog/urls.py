from django.urls import path
from .views import BlogPostListView, BlogPostDetailView
from. import views

urlpatterns = [
    path('', BlogPostListView.as_view(), name='blogpost_list'),
    path('post/<int:pk>/', BlogPostDetailView.as_view(), name='blog_detail'),
]
