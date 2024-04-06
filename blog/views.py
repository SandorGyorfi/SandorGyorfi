from django.views.generic import ListView, DetailView
from .models import BlogPost, Category

class BlogPostListView(ListView):
    model = BlogPost
    template_name = 'blog/blogpost_list.html'
    context_object_name = 'blogposts'
    paginate_by = 10

    def get_queryset(self):
        return BlogPost.objects.order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super(BlogPostListView, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

class BlogPostDetailView(DetailView):
    model = BlogPost
    template_name = 'blog/blogpost_detail.html'

    def get_context_data(self, **kwargs):
        context = super(BlogPostDetailView, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context
