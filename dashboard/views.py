from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from finances.models import Entry

# Create your views here.

@login_required
def dashboard_view(request):
    # Get user's entries
    entries = Entry.objects.filter(user=request.user)
    
    # Calculate total income and expenses
    total_income = sum(entry.amount for entry in entries if entry.type == Entry.INCOME)
    total_expenses = sum(entry.amount for entry in entries if entry.type == Entry.EXPENSE)
    balance = total_income - total_expenses
    
    context = {
        'total_income': total_income,
        'total_expenses': total_expenses,
        'balance': balance,
        'entries': entries[:5]  # Show only the 5 most recent entries
    }
    
    return render(request, 'dashboard/dashboard.html', context)
