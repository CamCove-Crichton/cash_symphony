from django.db import models
from profiles.models import UserProfile

class Expense(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    type = models.CharField(max_length=50)  # For types of expenses
    # Additional fields as needed

    class Meta:
        ordering = ['-date']  # Expenses will be ordered by date, most recent first

    def __str__(self):
        return f"{self.title} - {self.amount} - {self.date}"
