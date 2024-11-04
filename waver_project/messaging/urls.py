# messaging/urls.py

from django.urls import path
from .views import messaging_view

urlpatterns = [
    path('', messaging_view, name='messaging'),
]
