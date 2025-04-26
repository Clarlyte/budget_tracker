from django.db import models
from django.conf import settings

class Income(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    income = models.DecimalField(max_digits=12, decimal_places=2)
    date = models.DateField()

    def __str__(self):
        return f"{self.user.username} - {self.income} on {self.date}"

class Expense(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    category = models.CharField(max_length=100)
    expense = models.DecimalField(max_digits=12, decimal_places=2)
    date = models.DateField()
    description = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.category} - {self.expense} on {self.date}"
