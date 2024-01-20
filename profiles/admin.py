from django.contrib import admin
from .models import UserProfile
# Register your models here.


class ProfileAdmin(admin.ModelAdmin):
    """"""
    list_display = (
        'pk',
        'username',
        'profile_picture',
        'salary',
        'currency',

    )

admin.site.register(UserProfile, ProfileAdmin)
