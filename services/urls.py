from django.urls import path
from .views import services_view, service_detail_view

urlpatterns = [
    path('services/', services_view, name='services'),
    path('services/<int:pk>/', service_detail_view, name='service_detail'),
]
