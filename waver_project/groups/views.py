# groups/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Group  # Adjust import according to your actual Group model

@login_required
def groups_list(request):
    groups = Group.objects.all()  # Fetch all groups
    return render(request, 'groups/groups.html', {'groups': groups})

@login_required
def create_group(request):
    if request.method == 'POST':
        group_name = request.POST.get('group_name')
        Group.objects.create(name=group_name)  # Adjust based on your Group model
        return redirect('groups_list')
    return redirect('groups_list')
