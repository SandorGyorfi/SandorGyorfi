from django.contrib import admin
from .models import BlogPost, Category, Comment

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1
    raw_id_fields = ('author',)

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'updated_at')
    list_filter = ('created_at', 'author', 'categories')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'created_at'
    ordering = ('-created_at', 'author')
    filter_horizontal = ('categories',)
    inlines = [CommentInline]

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'body', 'post', 'created_on')
    list_filter = ('created_on', 'author')
    search_fields = ('body', 'author__username', 'post__title')
    raw_id_fields = ('author', 'post')

admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)
