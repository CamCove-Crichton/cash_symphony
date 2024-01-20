from datetime import datetime
import calendar
from decimal import Decimal
from home.models import Profile
from .models import Expense


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
    list_recurr_exp = Expense.objects.filter(indefinite=True).order_by('created_on')
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