from django.db import models


class ServiceRequest(models.Model):
    REQUEST_TYPES = (
        ('repair', 'Repair'),
        ('installation', 'Installation'),
        ('maintenance', 'Maintenance'),    
        ('billingissue', 'BillingIssue'),    
    )

    customer_name = models.CharField(max_length=100)
    customer_email = models.EmailField()
    request_type = models.CharField(max_length=20, choices=REQUEST_TYPES)
    description = models.TextField()
    file = models.FileField(upload_to='service_requests/', null=True, blank=True)
    status = models.CharField(max_length=20, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.customer_name} - {self.request_type}"
