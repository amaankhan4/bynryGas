from django.db import models
from django.contrib.auth.models import User

class ServiceRequest(models.Model):
    STATUS = [
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Resolved', 'Resolved'),
    ]
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='service_requests')
    request_type = models.CharField(max_length=100)
    description = models.TextField()
    attachment = models.FileField(upload_to='attachments/', blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)
    resolved_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.request_type} : {self.customer.username}"
