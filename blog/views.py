from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.views.generic import ListView, DetailView
from django.urls import reverse
from django.views.decorators.http import require_POST
from.models import BlogPost, Category
from.forms import BlogPostVoteForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
import json



class BlogPostListView(ListView):
    model = BlogPost
    template_name = 'blog/blogpost_list.html'
    context_object_name = 'blogposts'
    paginate_by = 3

    def get_queryset(self):
        return super().get_queryset().order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['vote_form'] = BlogPostVoteForm()
        context['choices'] = ['needs_work', 'meh', 'interesting', 'game_changer']
        return context


class BlogPostDetailView(DetailView):
    model = BlogPost
    template_name = 'blog/blogpost_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        blogpost = context.get('blogpost')

        friendly_names = {
            'needs_work': 'Needs Work',
            'meh': 'Meeeh',
            'interesting': 'Interesting',
            'game_changer': 'Game Changer'
        }
        
        context['choices'] = friendly_names  
        context['vote_form'] = BlogPostVoteForm()

        total_votes = sum(getattr(blogpost, f"{choice}_votes") for choice in friendly_names)
        context['vote_percentages'] = {
            choice: (getattr(blogpost, f"{choice}_votes") / total_votes * 100 if total_votes > 0 else 0)
            for choice in friendly_names 
        }

        return context



@require_POST
def submit_vote(request, pk):
    if not request.user.is_authenticated:
        return JsonResponse({'error': 'Authentication required'}, status=403)

    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)

    try:
        friendly_to_system = {
            'needs_work': 'needs_work',
            'meh': 'meh',
            'interesting': 'interesting',
            'game_changer': 'game_changer'
        }

        vote_type = data.get('vote')
        system_vote_type = friendly_to_system.get(vote_type)

        if system_vote_type is None:
            return JsonResponse({'error': 'Invalid vote type'}, status=400)

        blog_post = get_object_or_404(BlogPost, pk=pk)
        current_votes = getattr(blog_post, f'{system_vote_type}_votes', 0)
        setattr(blog_post, f'{system_vote_type}_votes', current_votes + 1)
        blog_post.save()

        vote_counts = {choice: getattr(blog_post, f'{choice}_votes') for choice in friendly_to_system.values()}
        total_votes = sum(vote_counts.values())
        percentages = {k: (v / total_votes * 100 if total_votes > 0 else 0) for k, v in vote_counts.items()}

        return JsonResponse({'success': True, 'percentages': percentages})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
