from django.contrib import admin
from .models import BlogPost, Category, Poll, PollOption, Vote

class PollOptionInline(admin.TabularInline):
    model = PollOption
    extra = 4  

class PollAdmin(admin.ModelAdmin):
    list_display = ('blog_post', 'question')
    inlines = [PollOptionInline]

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'updated_at')
    list_filter = ('created_at', 'author', 'categories')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'created_at'
    ordering = ('-created_at', 'author')
    filter_horizontal = ('categories',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class PollOptionAdmin(admin.ModelAdmin):
    list_display = ('poll', 'option_text', 'votes')
    list_filter = ('poll',)
    search_fields = ('option_text',)

class VoteAdmin(admin.ModelAdmin):
    list_display = ('poll_option', 'user', 'timestamp')
    list_filter = ('poll_option', 'timestamp')
    search_fields = ('poll_option__option_text', 'user__username')

# Register your models here.
admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Poll, PollAdmin)
admin.site.register(PollOption, PollOptionAdmin)
admin.site.register(Vote, VoteAdmin)
