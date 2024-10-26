from django.urls import path
from .views import home, register, login  # Импортируйте необходимые представления

urlpatterns = [
   path('', home, name='home'),  # Главная страница
   path('register/', register, name='register'),  # Страница регистрации
   path('login/', login, name='login'),  # Страница логина
]
