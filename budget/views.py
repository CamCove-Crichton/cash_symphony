from django.shortcuts import render
from .functions import get_outgoing_expense, get_remaining_budget


"""
Two functions are available here.
happy coding!!

get_remaining_budget(1, 1, 2024)
    arg: request.user.id(int), month(int), year(int)
    return: string
please comment
line 5 and the bottom of functions.py when profile's done.

get_outgoing_expense((2024, 1))
    arg: tuple(int: year, int: str)
    return string "xxx.xx"
"""

def view_budget(request):
    """
    A view to render the users budget
    """
    context = {

    }
    template = 'budget/budget.html'

    return render(request, template, context)
