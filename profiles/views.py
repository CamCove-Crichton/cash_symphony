from typing import Any
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView, UpdateView
from .models import UserProfile
from .forms import ProfileForm


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
        form.save()
        pk = self.kwargs["pk"]
        self.success_url = f'/profiles/username/{pk}/'
        return super().form_valid(form)

    
    def test_func(self):
        profile = self.get_object()
        return self.request.user == profile.username

    