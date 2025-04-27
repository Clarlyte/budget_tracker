from django import forms
from .models import Income, Expense

class IncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = ['income', 'date']  # Only show income and date fields

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['category', 'expense', 'date', 'description']  # All fields for expense
