from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class UserProfile(models.Model):
    '''User profile'''
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=254)
    job_title = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=10)
    
