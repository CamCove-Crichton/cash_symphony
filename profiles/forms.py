from django import forms
from .models import UserProfile


class ProfileForm(forms.ModelForm):
    """Form to create a profile"""
    class Meta:
        model = UserProfile
        fields = ["profile_picture", "job_title", "salary", "location", "monthly_budget_limit", "currency"]

        labels = {
            "profile_picture": "Avatar",
            "job_title": "Job Title",
            "salary": "Salary",
            "currency": "Currency",
            "location": "Location",
            "monthly_budget_limit": "Monthly Budget Limit",

        }

