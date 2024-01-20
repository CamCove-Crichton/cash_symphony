from django.shortcuts import render
from .functions import get_num_of_weekly_payments, get_outgoing_expense


"""
Two functions are available here.
happy coding!!

get_remaining_budget(1, 1, 2024)
    arg: request.user.id(int), month(int), year(int)
    return: string
When Profile model is done, please comment
line 5 and the bottom of functions.py

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
