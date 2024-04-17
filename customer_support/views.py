from django.shortcuts import render, get_object_or_404
from service_requests.models import ServiceRequest


def manager(request):   
    print('manager')
    return render(request, 'customer_support/manager.html')

def manage(request):
    servicerequests = ServiceRequest.objects.all()

    context = {'servicerequests': servicerequests}   
    
    return render(request, 'customer_support/manage_requests.html', context)

def update_request_status(request, request_id):
    service_request = get_object_or_404(ServiceRequest, id=request_id)
    if request.method == 'POST':
        status = request.POST.get('status')
        service_request.status = status
        service_request.save()
       
    return render(request, 'customer_support/update_request_status.html', {'request': service_request})