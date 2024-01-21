
from django import forms
from .models import Expense
from django.utils import timezone


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['title', 'amount', 'date', 'type']  # Add other fields you want to include in the form
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'max': timezone.localdate()}),
            # ... other widgets if needed
        }
