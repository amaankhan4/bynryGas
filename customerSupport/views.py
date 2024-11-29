from django.shortcuts import render, get_object_or_404
from services.models import ServiceRequest
from django.utils.timezone import now
from django.shortcuts import redirect
from django.contrib import messages


def dashboard(request):
    requests = ServiceRequest.objects.all()
    return render(request, 'customerSupport/dashboard.html', {'requests': requests})

def resolve_request(request, request_id):
    if request.method == "POST":
        # Get the specific service request
        service_request = get_object_or_404(ServiceRequest, request_id=request_id)
        
        # Update the status and resolved_at timestamp
        service_request.status = 'Resolved'
        service_request.resolved_at = now()
        service_request.save()
        
        # Add a success message (optional)
        messages.success(request, f"Request {request_id} marked as resolved.")
        
    # Redirect back to the dashboard
    return redirect('dashboard')
