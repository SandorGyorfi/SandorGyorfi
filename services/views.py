from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Service

def services_view(request):
    services_list = Service.objects.all()
    paginator = Paginator(services_list, 10)  
    page_number = request.GET.get('page')
    services = paginator.get_page(page_number)
    return render(request, 'services/services.html', {'services': services})

def service_detail_view(request, pk):
    service = get_object_or_404(Service, pk=pk)
    return render(request, 'services/service_detail.html', {'service': service})
