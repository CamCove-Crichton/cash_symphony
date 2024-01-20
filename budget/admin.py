"""This module holds classes to customize the admin panel."""

from django.contrib import admin
from django.db import models
from .models import Expense


@admin.register(Expense)
class ExpenseAdmin(models.ModelAdmin):
    """
    Customize the list, search and filter items of Expense model
    on the admin panel.
    """
    list_display = ('owner', 'name', 'amount', 'payment_date', 'type', 'budget_month', 'created_on')
    list_filter = ('owner', 'budget_month')
