from django.db import models

class Item(models.Model):
    States =[
        ('Available', 'available'),
        ('Sold Out', 'sold out'),
    ]
    name = models.CharField(max_length=128)
    slug = models.SlugField(max_length=128)
    cathegory = models.CharField(max_length=50)
    quantity = models.IntegerField(default=0)
    price = models.FloatField(default=0.0)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=25, choices=States)
    thumbnail = models.ImageField(upload_to='products', blank=True, null=True)

    def __str__(self) -> str:
        return self.name