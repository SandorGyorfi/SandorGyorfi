from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, Http404
from django.views.generic import View
import requests
import json

class BlogPostListView(View):
    def get(self, request):
        tumblr_api_url = "https://api.tumblr.com/v2/blog/your-tumblr-blog.tumblr.com/posts"
        tumblr_posts = []
        try:
            tumblr_response = requests.get(tumblr_api_url, params={'api_key': 'your_tumblr_api_key', 'limit': 10})
            tumblr_response_json = tumblr_response.json()
            if isinstance(tumblr_response_json, dict) and 'response' in tumblr_response_json:
                tumblr_posts = tumblr_response_json['response'].get('posts', [])
        except Exception as e:
            print(f"Error fetching Tumblr posts: {e}")

        context = {
            'tumblr_posts': tumblr_posts
        }
        return render(request, 'blog/blogpost_list.html', context)

class TumblrPostDetailView(View):
    def get(self, request, post_id):
        tumblr_api_url = f"https://api.tumblr.com/v2/blog/your-tumblr-blog.tumblr.com/posts/{post_id}"
        post_detail = {}
        try:
            response = requests.get(tumblr_api_url, params={'api_key': 'your_tumblr_api_key'})
            response_json = response.json()
            if isinstance(response_json, dict) and 'response' in response_json:
                posts = response_json['response'].get('posts', [])
                if posts:
                    post_detail = posts[0]
                else:
                    raise Http404("Post not found")
        except Exception as e:
            print(f"Error fetching Tumblr post detail: {e}")
            raise Http404("Error fetching post details")

        return render(request, 'blog/tumblr_post_detail.html', {'post_detail': post_detail})
