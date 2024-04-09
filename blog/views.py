from django.views.generic import ListView, DetailView
from .models import BlogPost, Category, Comment
from .forms import CommentForm
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required


class BlogPostListView(ListView):
    model = BlogPost
    template_name = 'blog/blogpost_list.html'
    context_object_name = 'blogposts'
    paginate_by = 3

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
        context = super().get_context_data(**kwargs)
        context['comments'] = self.object.comments.filter(parent__isnull=True)
        context['comment_form'] = CommentForm()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = self.object
            # Check if it's a reply
            if 'parent_id' in request.POST:
                comment.parent_id = request.POST.get('parent_id')
            comment.save()
            # Redirect to the post detail page
            return HttpResponseRedirect(self.object.get_absolute_url())
        return self.get(request, *args, **kwargs)


@login_required
def post_reply(request, blogpost_id):
    blogpost = get_object_or_404(BlogPost, pk=blogpost_id)
    if request.method == "POST":
        body = request.POST.get('reply_body')
        parent_id = request.POST.get('parent_id')
        parent_comment = get_object_or_404(Comment, pk=parent_id)
        # Assuming the Comment model has a 'user' field to denote the author of the comment
        Comment.objects.create(post=blogpost, author=request.user, body=body, parent=parent_comment)
    return redirect(blogpost.get_absolute_url())