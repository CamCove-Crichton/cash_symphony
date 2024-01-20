from django.shortcuts import render
from .functions import get_outgoing_expense, get_remaining_budget

"""
 following two functions are available.
 Please comment the code at the bottom of functions.py
 when Profile model is done.
 (imported from functions.py)
 get_outgoing_expense((2024, 1))  arg: tuple of year & month; return string
 get_remaining_budget(2, 1, 2024)  arg: user.id, month, year return string
"""

def view_budget(request):
    """
    A view to render the users budget
    """
    context = {

    }
    template = 'budget/budget.html'

    return render(request, template, context)
