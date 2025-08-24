from django.db import models
from django.urls import reverse
from Users.models import CustomUser

class Item(models.Model):
    States =[
        ('Available', 'available'),
        ('Sold Out', 'sold out'),
    ]
    name = models.CharField(max_length=128)
    slug = models.SlugField(max_length=128, default="", null=False)
    cathegory = models.CharField(max_length=50)
    quantity = models.IntegerField(default=0)
    price = models.FloatField(default=0.0)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=25, choices=States)
    thumbnail = models.ImageField(upload_to='products', blank=True, null=True)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='owned_items')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name
    
    
    def get_absolute_url(self):
        
        return reverse('product', kwargs={'slug':self.slug})