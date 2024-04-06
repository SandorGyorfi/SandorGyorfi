from django.contrib import admin
from .models import BlogPost, Category

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'updated_at')  
    list_filter = ('created_at', 'author', 'categories')  
    search_fields = ('title', 'content') 
    prepopulated_fields = {'slug': ('title',)}  
    raw_id_fields = ('author',)  
    date_hierarchy = 'created_at'  
    ordering = ('created_at', 'author')  
    filter_horizontal = ('categories',)  

admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Category)  
