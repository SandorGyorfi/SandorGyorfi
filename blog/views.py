from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView

from .forms import CommentForm
from .models import BlogPost, Category, Comment

class BlogPostListView(ListView):
    """Displays a list of Blog Posts ordered by creation date."""
    model = BlogPost
    template_name = 'blog/blogpost_list.html'
    context_object_name = 'blogposts'
    paginate_by = 3

    def get_queryset(self):
        """Return Blog Posts ordered by creation date."""
        return super().get_queryset().order_by('-created_at')

    def get_context_data(self, **kwargs):
        """Add categories to the context."""
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

class BlogPostDetailView(DetailView):
    """Displays a single Blog Post detail, along with comments and a form for new comments."""
    model = BlogPost
    template_name = 'blog/blogpost_detail.html'

    def get_context_data(self, **kwargs):
        """Add comments and a comment form to the context."""
        context = super().get_context_data(**kwargs)
        context['comments'] = self.object.comments.filter(parent__isnull=True)
        context['comment_form'] = CommentForm()
        return context

    def post(self, request, *args, **kwargs):
        """Handle POST requests to save a new comment."""
        self.object = self.get_object()
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = self.object
            if 'parent_id' in request.POST:
                comment.parent_id = request.POST.get('parent_id')
            comment.save()
            return HttpResponseRedirect(self.object.get_absolute_url())
        return self.get(request, *args, **kwargs)

@method_decorator(login_required, name='dispatch')
def post_reply(request, blogpost_id):
    """Handle POST requests to save a reply to a comment."""
    blogpost = get_object_or_404(BlogPost, pk=blogpost_id)
    if request.method == "POST":
        body = request.POST.get('reply_body')
        parent_id = request.POST.get('parent_id')
        parent_comment = get_object_or_404(Comment, pk=parent_id)
        Comment.objects.create(post=blogpost, author=request.user, body=body, parent=parent_comment)
    return redirect(blogpost.get_absolute_url())
