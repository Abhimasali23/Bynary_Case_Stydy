from django.shortcuts import render, redirect
from .forms import ServiceRequestForm
from .models import ServiceRequest
from django.db.models import Q

def home(request):

    servicerequests = ServiceRequest.objects.all()

    context = {'servicerequests': servicerequests}
    
    return render(request, 'service_requests/home.html', context)

def submit_request(request):
    form = ServiceRequestForm(request.POST, request.FILES)
    
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('request_submitted')
    else:
        form = ServiceRequestForm()

    context = {'form': form}
    return render(request, 'service_requests/submit_request.html', context)


def request_submitted(request):
    return render(request, 'service_requests/request_submitted.html')


def track_request(request):

    q = request.GET.get('q') if request.GET.get('q') != None else ''

    servicerequests = ServiceRequest.objects.filter(
        Q(customer_email__icontains=q) |
        Q(customer_name__icontains=q)
    )

    context = {'servicerequests': servicerequests}
    
    return render(request, 'service_requests/track_request.html', context)


def update_request(request, pk):
    requests = ServiceRequest.objects.get(id=pk)
    form = ServiceRequestForm(instance=requests)
    

    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES, instance=requests)
        
        if form.is_valid():            
            form.save()
            return redirect('home')
    
    context = {'form': form}
    return render(request, 'service_requests/submit_request.html', context)

def customer(request):
    return render(request, 'service_requests/customer.html')









