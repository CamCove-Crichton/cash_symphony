from datetime import datetime
import calendar
from decimal import Decimal
from .models import Expense
from home.models import Profile


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


def get_outgoing_expense(year_and_month):
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
    format = format = '%Y-%m-%d'
    first_day_month = datetime.strptime(f"{year}-{str_month}-01", format)
    # datetime obj of last day of the month
    last_day_month = first_day_month.replace(day=num_days_month)
    # get the first day of the following month
    nextMonth = month + 1
    if month == 12:
        nextMonth = 1
    first_day_next_month = first_day_month.replace(month=nextMonth)
    # get expenses for the current month. (once off)
    list_once_off_exp = Expense.objects.filter(budget_month=f"{year}-{month}").order_by('payment_date')
    # get the sum of once-off expenses for the month
    sum_once_off_exp = sum(Decimal(expense.amount) for expense in list_once_off_exp)
    # get regularly recurring expenses that will happen in the current month
    # (those with 'frequency' value of daily, weekly or monthly AND
    #  that haven't been stopped earlier than that month)
    list_recurr_exp = Expense.objects.filter(type="recurring", end_date__gte=first_day_month).order_by('created_on')
    list_recurr_exp = []
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
    sum_decimal = sum_once_off_exp + sum_recurr_exp
    sum_str = str("{:.2f}".format(sum_decimal))
    return sum_str


def get_remaining_budget(user_id, month, year):
    """
    calculate remaining budget and return it.

    Argument user_id
    Return remaining budget
    Rtype string
    """
    """
    income = Profile.objects.filter(id=user_id)[0].income
    spending = get_outgoing_expense((year, month))
    return Decimal(income) - Decimal(spending)
    """
