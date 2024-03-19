from django.shortcuts import render
from blog.models import BlogPost
from services.models import Service  

def home_view(request):
    latest_blog_posts = BlogPost.objects.order_by('-created_at')[:3]
    services = Service.objects.all()[:3] 
    context = {
        'latest_blog_posts': latest_blog_posts,
        'services': services,
    }
    return render(request, 'home/home.html', context)
