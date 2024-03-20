from django.shortcuts import render
from .models import Service

def services_view(request):
    services = Service.objects.all()
    return render(request, 'services/services.html', {'services': services})
