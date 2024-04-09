from django.urls import path
from .views import BlogPostListView, BlogPostDetailView, post_reply


urlpatterns = [
    path('', BlogPostListView.as_view(), name='blogpost_list'),
    path('post/<int:pk>/', BlogPostDetailView.as_view(), name='blog_detail'),
    path('post/<int:blogpost_id>/reply/', post_reply, name='post_reply'),

]
