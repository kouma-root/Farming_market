from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class CustomUser(AbstractUser):
    
    status ={
        ('Farmer', 'farmer'),
        ('Buyer', 'buyer'),
    }
    locate = {
        ('NG', 'Nigeria'),
        ('CM', 'Cameroon'),
        ('GH', 'Ghana'),
        ('US', 'United State'),
        ('UK', 'United Kingdom'),
        ('FR', 'France'),
        ('RU', 'Russia'),
    }
    username = models.CharField(max_length=200, unique=True)
    email = models.EmailField(unique=True, max_length=254)
    role = models.CharField(max_length=7,choices= status)
    location = models.CharField(max_length=20,choices= locate)
    phone_number = models.CharField(max_length=15)
    create_at = models.DateTimeField(default= timezone.now)
    
    USERNAME_FIELD= 'email'
    REQUIRED_FIELDS = ['username']