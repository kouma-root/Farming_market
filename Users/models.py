from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
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
    create_at = models.DateTimeField(default= timezone.now, editable=False)
    
    USERNAME_FIELD= 'email'
    REQUIRED_FIELDS = ['username']
    
    def __str__(self) -> str:
        return self.username
    
    
class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    is_farmer = models.BooleanField(default=False)
    is_buyer = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return self.user.username
    
    
@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        is_farmer = instance.role == 'Farmer'
        is_buyer = instance.role == 'Buyer'
        Profile.objects.create(user=instance, is_farmer=is_farmer, is_buyer=is_buyer)
        
@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()