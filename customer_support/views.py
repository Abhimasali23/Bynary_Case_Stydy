from django.shortcuts import render, get_object_or_404, redirect
from service_requests.models import ServiceRequest
from service_requests.forms import ServiceRequestForm


def manager(request):   
    print('manager')
    return render(request, 'customer_support/manager.html')

def manage(request):
    servicerequests = ServiceRequest.objects.all()

    context = {'servicerequests': servicerequests}   
    
    return render(request, 'customer_support/manage_requests.html', context)

def update_request(request, pk):
    requests = ServiceRequest.objects.get(id=pk)
    form = ServiceRequestForm(instance=requests)
    

    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES, instance=requests)
        
        if form.is_valid():            
            form.save()
            return redirect('manage')
    
    context = {'form': form}
    return render(request, 'service_requests/submit_request.html', context)


def delete_request(request, pk):
    requests = ServiceRequest.objects.get(id=pk)
    if request.method == 'POST':
        requests.delete()
        return redirect('manage')

    context = {'item': requests}
    return render(request, 'customer_support/delete.html', context)