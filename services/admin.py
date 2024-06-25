from django.contrib import admin
from .models import Service

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'short_description', 'home_description')
    search_fields = ('title', 'short_description')
    list_filter = ('title',)
    ordering = ('title',)
    fieldsets = (
        (None, {
            'fields': ('title', 'short_description', 'description', 'home_description', 'link')
        }),
    )
