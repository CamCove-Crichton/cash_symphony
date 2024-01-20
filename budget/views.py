from django.shortcuts import render
from .functions import get_num_of_weekly_payments, get_outgoing_expense


"""
two functions are available here.
happy coding!!

(1, 1, 2024)
    arg: request.user.id(int), month(int), year(int)
    return: string
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
