from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Friend
from django.contrib.auth.decorators import login_required

@login_required
def add_friend(request, user_id):
    friend = User.objects.get(id=user_id)
    if not Friend.objects.filter(user=request.user, friend=friend).exists() and request.user != friend:
        Friend.objects.create(user=request.user, friend=friend)
    return redirect('home')

@login_required
def remove_friend(request, user_id):
    friend = User.objects.get(id=user_id)
    Friend.objects.filter(user=request.user, friend=friend).delete()
    return redirect('home')
