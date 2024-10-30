from django.urls import path
from . import views
from .views import home, register, login

urlpatterns = [
   path('', home, name='home'),  # Главная страница
   path('register/', register, name='register'),  # Страница регистрации
   path('login/', login, name='login'),  # Страница логина
   path('friend-request/send/<int:to_user_id>/', views.send_friend_request, name='send_friend_request'),
   path('friend-request/accept/<int:request_id>/', views.accept_friend_request, name='accept_friend_request'),
   path('friend-request/reject/<int:request_id>/', views.reject_friend_request, name='reject_friend_request'),
]
