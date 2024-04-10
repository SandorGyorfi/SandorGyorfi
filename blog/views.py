from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from .models import BlogPost, PollOption
from django.http import JsonResponse



from .forms import PollResponseForm
from .models import BlogPost, Category, Poll, PollOption

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
    model = BlogPost
    template_name = 'blog/blogpost_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        poll = Poll.objects.filter(blog_post=self.object).first()
        if poll:
            context['poll_form'] = PollResponseForm(poll_id=poll.id)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        poll = Poll.objects.filter(blog_post=self.object).first()
        if poll:
            form = PollResponseForm(request.POST, poll_id=poll.id)
            if form.is_valid():
                selected_option = form.cleaned_data['option']
                selected_option.votes += 1
                selected_option.save()
                return redirect('blog:blog_detail', pk=self.object.pk)
        return super().get(request, *args, **kwargs)
    
def submit_vote(request, pk):
    if request.method == 'POST':
        blog_post = get_object_or_404(BlogPost, pk=pk)
        option_id = request.POST.get('option')
        selected_option = get_object_or_404(PollOption, id=option_id)
        
        selected_option.votes += 1
        selected_option.save()

        poll_options = blog_post.poll.options.all()
        data = {
            'pollOptions': [{
                'id': option.id,
                'percentage': (option.votes / sum(o.votes for o in poll_options) * 100) if poll_options else 0
            } for option in poll_options]
        }

        return JsonResponse(data)

    # Handle non-POST requests or other error cases
    return JsonResponse({'error': 'Invalid request'}, status=400)    
