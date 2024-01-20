from django.views.generic import TemplateView, View
from django.shortcuts import render
from datetime import datetime
import calendar
from decimal import Decimal


class Index(TemplateView):
    template_name = 'home/index.html'


"""
If you will test the function, please enter some expense data (line 38-59),
put them in 1) list of once off payments and in 2) list of recurring payments
and call calculateOutgoingExpenses((2024, 1)) for example for 2024 January
at the bottom of this code (line 161)

part up to line 59 will be removed for production.

"""
class Expense:
    """
    the following class is only to make some dummy expense data.
    We need to make django model.  need to come up with right fields later.
    also need budget_month (for once_off expenses only, to show
    the budjet of which month the data belongs to), created_on...etc
    """
    def __init__(self, name, amount, payment_type, payment_date, frequency, start_date, end_date):
        self.name = name
        self.amount = amount
        self.payment_type = payment_type # recurring or once off
        self.payment_date = payment_date # no need to fill if recurring
        # below are only for recurring expenses
        # if once_off, leave them "" or None.
        self.frequency = frequency # daily, weekly, monthly or ""
        self.start_date = start_date
        self.end_date = end_date

 # for now, using Expense class, make some dummy data.
# first make some datetime obj
format = format = '%Y-%m-%d'
date1 = datetime.strptime("2024-01-05", format)
date2 = datetime.strptime("2024-01-07", format)
date3 = datetime.strptime("2024-01-08", format)
# Expense class objects (name, amount, type, payment_date, frequency, start_date, end_date)
exp1 = Expense("exp1", "19.95", "once_off", date1, "", None, None)
exp2 = Expense("exp2", "55.25", "once_off", date2, "", None, None)
# put them in list of once off expenses
list_once_off_exp = [exp1, exp2]

# make expense obj for recurring payments and put them in
# the list of recurring expenses
date3 = datetime.strptime("2023-12-01", format)
date4 = datetime.strptime("2024-01-01", format)
date5 = datetime.strptime("2024-03-31", format)
# Expense class objects (name, amount, type, payment_date, frequency, start_date, end_date)
exp3 = Expense("exp3", "20.45", "recurring", None, "daily", date3, date4)
exp4 = Expense("exp4", "90.00", "recurring", None, "weekly", date4, date5)
exp5 = Expense("exp5", "1000.00", "recurring", None, "monthly", date3, None)

list_recurr_exp = [exp3, exp4, exp5]


def get_num_of_weekly_payments(start_date, first_day, last_day):
    """
    Calculate and return the number of times
    a given weekly payment will be made in the month.

    Args:
        start_date (datetime): the start date of the expense entry
        first_day (datetime): the fist day of the time period of interedst
        last_day (datetime): the last day of the time period

    Returns:
        int: number of times that the given payment will be made in the month
    """
    # get the weekday of the 1st day of the time period
    wd_start = first_day.weekday()
    # get the weekday of the last day in the time period
    wd_end = last_day.weekday()
    # get the weekday that we're counting
    wd_target = start_date.weekday()
    # how many of the specific weekday we have in the time period
    num_occ = round((last_day.day - first_day.day) / 7)
    if wd_start < wd_target < wd_end:
        # in this condition, you get an extra day
        num_occ += 1
    return num_occ


def calculateOutgoingExpense(year_and_month):
    """
    calculate and return the sum of outgoing expenses
    in a given month

    Argument: tuple of year and month (int, int)
    :return: sum of outgoing expenses
    :rtype: string
    """
    # get the year and month of interest
    year = year_and_month[0]
    month = year_and_month[1]
    # get the number of days in the month (28, 29, 30, 31...)
    num_days_month = calendar.monthrange(year, month)[1]
    if len(str(month)) == 1:
        str_month = f"0{month}"
    # create datetime object of the first of that month
    first_day_month = datetime.strptime(f"{year}-{str_month}-01", format)
    # datetime obj of last day of the month
    last_day_month = first_day_month.replace(day=num_days_month)
    # get the first day of the following month
    nextMonth = month + 1
    if month == 12:
        nextMonth = 1
    first_day_next_month = first_day_month.replace(month=nextMonth)

    # get expenses for the current month. (once off & recurring but irregular ones)
    """
    list_once_off_exp = Expense.objects.filter(budget_month=f"{year}-{month}")
                                .order_by('payment_date')
    """
    # get the sum of once-off expenses for the month
    sum_once_off_exp = sum(Decimal(expense.amount) for expense in list_once_off_exp)

    # get regularly recurring expenses that will happen in the current month
    # (those with 'frequency' value of daily, weekly or monthly AND
    #  that haven't been stopped earlier than that month)
    """
    list_recurr_exp = Expense.objects.filter(frequency!="",
                            (end_date=None | end_date__gt=first_day_month))
                            .order_by('created_on')
    """
    sum_recurr_exp = 0
    last_day = None
    first_day = None
    # get sum of recurring expenses in the given month
    for item in list_recurr_exp:
        # if end_date is None or after this month,
        # set the last_day_month as last_day
        # otherwise set it to the item.end_date
        if item.end_date == None:
            last_day = last_day_month
        elif item.end_date >= first_day_next_month:
            last_day = last_day_month
        else:
            last_day = item.end_date
        # set first_day
        first_day = item.start_date
        if item.start_date < first_day_month:
            first_day = first_day_month

        # for each 'frequency' value, get the number of occurrences
        if item.frequency == "daily":
            num_occ = last_day.day - first_day.day + 1
        elif item.frequency == "weekly":
            num_occ = get_num_of_weekly_payments(item.start_date, first_day, last_day)
        else:
            # if 'monthly'
            num_occ = 1
        sum_recurr_exp += Decimal(item.amount) * num_occ
    sum_int = sum_once_off_exp + sum_recurr_exp
    sum_str = str("{:.2f}".format(sum_int))
    return sum_str

print("test calculateOutgoingExpense in views.py")
print(calculateOutgoingExpense((2024, 1)))
