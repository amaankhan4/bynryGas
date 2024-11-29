from django.shortcuts import render, get_object_or_404
from services.models import ServiceRequest
from django.contrib.admin.views.decorators import staff_member_required

@staff_member_required
def dashboard(request):
    requests = ServiceRequest.objects.all()
    return render(request, 'customerSupport/dashboard.html', {'requests': requests})
