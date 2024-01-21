"""This module holds forms used in cash symphony."""
from .models import Expense
from django import forms


class ExpenseForm(forms.ModelForm):
    """Form for expense entries."""
    class Meta:
        """defines features of ExpenseForm."""
        model = Expense
        fields = ['name', 'amount', 'payment_date',
                  'payment_type', 'budget_month', 'frequency',
                  'start_date', 'end_date']
        name = forms.CharField(required=True)
        amount = forms.CharField(required=True)
        payment_type = forms.IntegerField(required=True)
