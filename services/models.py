from django.db import models
from django.contrib import admin
import random

class ServiceRequest(models.Model):
    def generate_request_id():
        while True:
            newId = random.randint(1000000000, 9999999999)
            if not ServiceRequest.objects.filter(request_id=newId).exists():
                return newId

    STATUS = [
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Resolved', 'Resolved'),
    ]

    REQ_TYPES = [
        ('Technical Support', 'Technical Support'),
        ('Bill Payment Inquiry', 'Bill Payment Inquiry'),
        ('Scheduled Maintenance Inquiry', 'Scheduled Maintenance Inquiry'),
        ('Change of Address', 'Change of Address'),
        ('Feature Request', 'Feature Request'),
        ('Other', 'Other'),

    ]

    request_id = models.BigIntegerField(primary_key=True, default=generate_request_id, editable=False)
    email = models.EmailField()
    request_type = models.CharField(choices=REQ_TYPES, default="Technical Support", max_length=50)
    description = models.TextField()
    attachment = models.FileField(upload_to='attachments/', blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)
    resolved_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.request_id} : {self.request_type}"
    
    
admin.site.register(ServiceRequest)
