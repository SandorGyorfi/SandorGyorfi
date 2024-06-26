from django.shortcuts import render
import requests

def home_view(request):
    tumblr_api_url = "https://api.tumblr.com/v2/blog/your-tumblr-blog.tumblr.com/posts"

    # Fetch latest blog posts from Tumblr
    tumblr_posts = []
    try:
        tumblr_response = requests.get(tumblr_api_url, params={'api_key': 'your_tumblr_api_key', 'limit': 3})
        tumblr_response_json = tumblr_response.json()
        if isinstance(tumblr_response_json, dict) and 'response' in tumblr_response_json:
            tumblr_posts = tumblr_response_json['response'].get('posts', [])
        elif isinstance(tumblr_response_json, list):
            tumblr_posts = tumblr_response_json
    except Exception as e:
        print(f"Error fetching Tumblr posts: {e}")

    context = {
        'tumblr_posts': tumblr_posts,
    }
    return render(request, 'home/home.html', context)
