from django.urls import path
from .views import BlogPostListView, BlogPostDetailView

from. import views

urlpatterns = [
    path('', BlogPostListView.as_view(), name='blogpost_list'),
    path('blog/', views.BlogPostListView.as_view(), name='blog_list'),
    path('blog/<int:pk>/', views.BlogPostDetailView.as_view(), name='blog_detail'),
]