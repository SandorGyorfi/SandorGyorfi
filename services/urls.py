from django.urls import path
from .views import services_view, service_detail_view

app_name = 'services'

urlpatterns = [
    path('', services_view, name='services'),
    path('<int:pk>/', service_detail_view, name='service_detail'),
]
