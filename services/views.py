from django.shortcuts import render, redirect, get_object_or_404
from .forms import ServiceRequestForm
from .models import ServiceRequest


def create_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.save()
            request_id = service_request.request_id
            return render(request, 'services/successful.html', {'request_id': request_id})
    else:
        form = ServiceRequestForm()
    return render(request, 'services/create_request.html', {'form': form})


def requestDetails(request,pk):
    result = get_object_or_404(ServiceRequest,pk=pk)
    return render(request,'services/request_details.html',{'result':result})
