from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from .forms import UserRegistrationForm, UserLoginForm


def register(request):
   if request.method == 'POST':
      form = UserRegistrationForm(request.POST)
      if form.is_valid():
         user = form.save()
         login(request, user)  # Вход пользователя после успешной регистрации
         return redirect('home')  # Переход на главную страницу
   else:
      form = UserRegistrationForm()
   return render(request, 'core/register.html', {'form': form})

def login(request):
   if request.method == 'POST':
      form = UserLoginForm(request.POST)
      if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
               auth_login(request, user)
               return redirect('home')  # Перенаправление на главную страницу
            else:
               messages.error(request, 'Неверные учетные данные.')
   else:
      form = UserLoginForm()
   return render(request, 'core/login.html', {'form': form})

def home(request):
   return render(request, 'core/home.html')