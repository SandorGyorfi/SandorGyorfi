from django.urls import path
from .views import BlogPostListView, TumblrPostDetailView

urlpatterns = [
    path('', BlogPostListView.as_view(), name='blogpost_list'),
    path('tumblr/post/<str:post_id>/', TumblrPostDetailView.as_view(), name='tumblr_post_detail'),
]