from django.urls import path
from . import views

#add urls here

app_name = 'finances'

urlpatterns = [
    path('expenses/', views.ExpenseListView.as_view(), name='expense_list'),  
    path('income/add/', views.IncomeCreateView.as_view(), name='income_add'), 
    path('expense/add/', views.ExpenseCreateView.as_view(), name='expense_add'),  
    path('expense/<int:pk>/delete/', views.ExpenseDeleteView.as_view(), name='expense_delete'),
]
