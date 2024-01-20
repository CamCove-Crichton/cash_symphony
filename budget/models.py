from django.db import models
from django.contrib.auth.models import User


# status of posts
TYPE = ((0, "once_off"), (1, "recurring"))
FREQUENCY = ((0, "NA"), (1, "daily"), (2, "weekly"), (3, "monthly"))


class Expense(models.Model):
    """Hold fields of Expense model and functions around them."""
    name = models.CharField(max_length=45)
    amount = models.CharField(max_length=12)
    owner = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name="expenses")
    type = models.IntegerField(choices=TYPE, default=0)
    payment_date = models.DateTimeField(null=True, blank=True)
    budget_month = models.CharField(max_length=7, null=True, blank=True)
    frequency = models.IntegerField(choices=FREQUENCY, default=0)
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['payment_date', 'created_on']

    def __str__(self):
        """
        Return the name.
        :return: name
        :rtype: str
        """
        return self.name
