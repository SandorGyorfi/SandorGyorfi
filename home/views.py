from django.shortcuts import render
from blog.models import BlogPost

def home_view(request):
    latest_blog_posts = BlogPost.objects.order_by('-created_at')[:3]

    context = {
        'latest_blog_posts': latest_blog_posts,
    }
    return render(request, 'home/home.html', context)
