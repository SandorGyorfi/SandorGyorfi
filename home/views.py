from django.shortcuts import render
import requests

def home_view(request):
    tumblr_api_url = "https://api.tumblr.com/v2/blog/your-tumblr-blog.tumblr.com/posts"
    media_blog_api_url = "https://your-media-blog-api-endpoint"

    # Fetch latest blog posts from Tumblr
    tumblr_posts = []
    try:
        tumblr_response = requests.get(tumblr_api_url, params={'api_key': 'your_tumblr_api_key', 'limit': 3})
        tumblr_response_json = tumblr_response.json()
        if isinstance(tumblr_response_json, dict) and 'response' in tumblr_response_json:
            tumblr_posts = tumblr_response_json['response'].get('posts', [])
    except Exception as e:
        print(f"Error fetching Tumblr posts: {e}")

    # Fetch latest posts from Media Blog
    media_blog_posts = []
    try:
        media_blog_response = requests.get(media_blog_api_url, params={'limit': 3})
        media_blog_response_json = media_blog_response.json()
        if isinstance(media_blog_response_json, dict) and 'posts' in media_blog_response_json:
            media_blog_posts = media_blog_response_json['posts']
    except Exception as e:
        print(f"Error fetching media blog posts: {e}")

    context = {
        'tumblr_posts': tumblr_posts,
        'media_blog_posts': media_blog_posts,
    }
    return render(request, 'home/home.html', context)