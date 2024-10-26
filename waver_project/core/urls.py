# core/urls.py
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import register, edit_profile

urlpatterns = [
   path('register/', register, name="register"),
   path('login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
   path('profile/edit/', edit_profile, name='edit_profile'),
   path('logout/', auth_views.LogoutView.as_view(), name='logout'),
   
]
