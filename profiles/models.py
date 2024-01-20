from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from django_resized import ResizedImageField

# Create your models here.


class UserProfile(models.Model):
    '''User profile'''
    username = models.ForeignKey(User,related_name="profile", on_delete=models.CASCADE)
    profile_picture = ResizedImageField(size=[300,300], quality=75, upload_to="profiles/", force_format="WEBP", blank=True)
    email = models.EmailField(max_length=254)
    job_title = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2, default="0" , blank=True, null=True)
    currency = models.CharField(max_length=10)
    monthly_budget_limit = models.DecimalField(max_digits=10, decimal_places=2, default="0", blank=True, null=True)

    def __str__(self):
        return str(self.username)
    

@receiver(post_save, sender=User)
def create_user_profile(instance, created, **kwargs):
    """Create or update the user profile"""
    if created:
        UserProfile.objects.create(username=instance)
    
