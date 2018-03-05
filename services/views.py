from django.shortcuts import render
from django.http import Http404
from services.models import Service, ServiceIndex



def ServicesPage(request):
    services_banner = ServiceIndex.objects.order_by('id')[0]
    services = Service.objects.all()
    return render(request, 'services/services.html',{
                'services_banner':services_banner,
                'services':services,
    })

def Service_Details(request, id):
    try:
        service = Service.objects.get(id=id)
    except Service.DoesNotExist:
        raise Http404('This service does not exist')
    return render(request, 'services/service_details.html',{
        'service':service,
    })
