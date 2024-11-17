from django.urls import path
from . import views

urlpatterns = [
    path('chat/<int:user_id>/', views.chat, name='chat'),
]
