from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

User = get_user_model()

class Category(models.Model):
    """Represents a category for blog posts."""
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class BlogPost(models.Model):
    """Represents a blog post."""
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=250, unique_for_date='created_at', null=True, blank=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    categories = models.ManyToManyField(Category, related_name='blog_posts')

    # Vote counters for each category
    needs_work_votes = models.PositiveIntegerField(default=0)
    meh_votes = models.PositiveIntegerField(default=0)
    interesting_votes = models.PositiveIntegerField(default=0)
    game_changer_votes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:blog_detail', args=[self.pk])

    def save(self, *args, **kwargs): 
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
