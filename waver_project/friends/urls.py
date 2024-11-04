# friends/urls.py

from django.urls import path
from .views import friends_list, add_friend

urlpatterns = [
    path('', friends_list, name='friends_list'),
    path('add/', add_friend, name='add_friend'),
]
