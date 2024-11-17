from django.shortcuts import render, redirect
from .models import Message
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

@login_required
def chat(request, user_id):
    user = User.objects.get(id=user_id)
    messages = Message.objects.filter(sender=request.user, receiver=user) | Message.objects.filter(sender=user, receiver=request.user)
    messages = messages.order_by('sent_at')

    if request.method == "POST":
        content = request.POST.get('message')
        if content:
            Message.objects.create(sender=request.user, receiver=user, content=content)
            return redirect('chat', user_id=user.id)

    return render(request, 'chat.html', {'user': user, 'messages': messages})
