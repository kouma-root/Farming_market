from django.db import models
from Users.models import CustomUser
from Product.models import Item
from django.utils import timezone


class Request(models.Model):
    
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    ]
    
    buyers = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='requests')
    product = models.ForeignKey(Item, on_delete= models.CASCADE, related_name='requests')
    quantity = models.PositiveIntegerField()
    message = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')
    created_at = models.DateTimeField(default= timezone.now, editable=False)

    
    def __str__(self):
        return f"Request by {self.buyers.username} for {self.product.name} - {self.status}"
    
    
