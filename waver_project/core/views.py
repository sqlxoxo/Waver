from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import UserProfileForm
from .models import UserProfile

def register(request):
   if request.method == 'POST':
      form = CustomUserCreationForm(request.POST)
      if form.is_valid():
            user = form.save()
            # Создание UserProfile после успешной регистрации
            UserProfile.objects.create(user=user)
            return redirect('login')  # Перенаправление на страницу входа
   else:
      form = CustomUserCreationForm()
   return render(request, 'core/register.html', {'form': form})


@login_required
def edit_profile(request):
   profile = request.user.userprofile
   if request.method == 'POST':
      form = UserProfileForm(request.POST, instance=profile)
      if form.is_valid():
            form.save()
            messages.success(request, 'Профиль успешно обновлён!')
            return redirect('edit_profile')  # Измените на URL вашего профиля
   else:
      form = UserProfileForm(instance=profile)
   return render(request, 'core/edit_profile.html', {'form': form})


@login_required  # Ограничим доступ только для авторизованных пользователей
def home(request):
   return render(request, 'core/home.html')