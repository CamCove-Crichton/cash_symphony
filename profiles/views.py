from typing import Any
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView, UpdateView
from .models import UserProfile
from .forms import ProfileForm
from django.contrib.auth.models import User
from django.urls import reverse



class Profiles(TemplateView):
    """User profile view"""
    template_name = "profiles/profile.html"
    
    def get_context_data(self, **kwargs):
        profile = UserProfile.objects.get(username__id=self.kwargs["pk"])
        context = {
            'profile': profile,
            'form': ProfileForm(instance=profile)
        }

        return context



class EditProfile(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """Edit a profile"""
    form_class = ProfileForm
    model = UserProfile

    def form_valid(self, form):
        self.success_url = reverse("profile", args=[str(self.kwargs["pk"])])
        return super().form_valid(form)
    

    def get_object(self, queryset=None):
        # If your ForeignKey in UserProfile is named `username` and has `related_name='profile'`:
        return UserProfile.objects.get(username__id=self.kwargs["pk"])

    def test_func(self):
        profile = self.get_object()
        return self.request.user == profile.username    


    # def get_object(self, queryset=None):
    #     user = User.objects.get(pk=self.kwargs["pk"])
    #     return user.profile

    # def test_func(self):
    #     return self.request.user == self.get_object().user

    # def form_valid(self, form):
    #     form.save()
    #     pk = self.kwargs["pk"]
    #     self.success_url = f'/profiles/username/{pk}/'
    #     return super().form_valid(form)

    
    # def test_func(self):
    #     profile = self.get_object()
    #     return self.request.user == profile.username

    