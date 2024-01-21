"""This module holds classes to customize the admin panel."""

from django.contrib import admin
from .models import Expense

"""
@admin.register(Expense)
class PostAdmin(admin.ModelAdmin):

    Customize the list, search and filter items of Expense model
    on the admin panel.

    list_display = ('user', 'name', 'amount', 'budget_month')
    list_filter = ('user', 'budget_month', 'type')
"""
