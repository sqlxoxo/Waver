# friends/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Friend  # Adjust import according to your actual Friend model

@login_required
def friends_list(request):
    friends = request.user.friends.all()  # Assuming you have a related name set for friends
    return render(request, 'friends/friends.html', {'friends': friends})

@login_required
def add_friend(request):
    if request.method == 'POST':
        friend_username = request.POST.get('friend_username')
        try:
            friend = User.objects.get(username=friend_username)
            request.user.friends.add(friend)  # Assuming you have a ManyToMany field for friends
            return redirect('friends_list')
        except User.DoesNotExist:
            # Handle the case where the user does not exist
            pass
    return redirect('friends_list')
