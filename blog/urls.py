from django.urls import path
from .views import BlogPostListView, BlogPostDetailView, submit_vote

urlpatterns = [
    path('', BlogPostListView.as_view(), name='blogpost_list'),
    path('post/<int:pk>/', BlogPostDetailView.as_view(), name='blog_detail'),
    path('post/<int:pk>/vote/', submit_vote, name='submit_vote'), 
]
