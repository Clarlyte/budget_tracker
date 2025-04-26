from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_entry, name='add_entry'),
    path('edit/<int:entry_id>/', views.edit_entry, name='edit_entry'),
    path('delete/<int:entry_id>/', views.delete_entry, name='delete_entry'),
    path('entries/', views.entry_list, name='entry_list'),
]
