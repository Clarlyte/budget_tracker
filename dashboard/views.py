from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def dashboard_view(request):
    context = {
        'total_income': 0,
        'total_expenses': 0,
        'balance': 0,
        'entries': []  # Empty list since we removed Entry model
    }
    
    return render(request, 'dashboard/dashboard.html', context)
