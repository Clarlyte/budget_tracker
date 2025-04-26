from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Entry  # You'll need to create this model

# Create your views here.

@login_required
def add_entry(request):
    if request.method == 'POST':
        # Handle form submission
        pass
    return render(request, 'finances/add_entry.html')

@login_required
def edit_entry(request, entry_id):
    entry = get_object_or_404(Entry, id=entry_id)
    if request.method == 'POST':
        # Handle form submission
        pass
    return render(request, 'finances/edit_entry.html', {'entry': entry})

@login_required
def delete_entry(request, entry_id):
    entry = get_object_or_404(Entry, id=entry_id)
    if request.method == 'POST':
        entry.delete()
        return redirect('entry_list')
    return render(request, 'finances/delete_entry.html', {'entry': entry})

@login_required
def entry_list(request):
    entries = Entry.objects.filter(user=request.user)
    return render(request, 'finances/entry_list.html', {'entries': entries})
