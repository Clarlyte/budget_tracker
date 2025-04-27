from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, DeleteView
from django.urls import reverse_lazy
from .models import Income, Expense
from .forms import IncomeForm, ExpenseForm
from django.contrib.auth.mixins import LoginRequiredMixin


class ExpenseListView(LoginRequiredMixin, ListView):
    model = Expense
    template_name = 'finances/expense_list.html'  
    context_object_name = 'expenses'

    def get_queryset(self):
       
        return Expense.objects.filter(user=self.request.user)


class IncomeCreateView(LoginRequiredMixin, CreateView):
    model = Income
    form_class = IncomeForm
    template_name = 'finances/income_form.html'  
    success_url = reverse_lazy('finances:expense_list')  

    def form_valid(self, form):
        form.instance.user = self.request.user  
        return super().form_valid(form)


class ExpenseCreateView(LoginRequiredMixin, CreateView):
    model = Expense
    form_class = ExpenseForm
    template_name = 'finances/expense_form.html'  
    success_url = reverse_lazy('finances:expense_list') 
    def form_valid(self, form):
        form.instance.user = self.request.user  
        return super().form_valid(form)


class ExpenseDeleteView(LoginRequiredMixin, DeleteView):
    model = Expense
    template_name = 'finances/expense_confirm_delete.html' 
    success_url = reverse_lazy('finances:expense_list')  
