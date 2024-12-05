from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('register/', views.register, name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('login/', views.user_login, name='login'),
]
