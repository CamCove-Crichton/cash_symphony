"""This module holds classes to customize the admin panel."""

from django.contrib import admin
from .models import Expense

@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    """Customize the list, search and filter items of Expense model
    on the admin panel."""

    list_display = ('owner', 'name', 'amount', 'budget_month')
    list_filter = ('owner', 'budget_month', 'payment_type')
