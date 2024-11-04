# groups/urls.py

from django.urls import path
from .views import groups_list, create_group

urlpatterns = [
    path('', groups_list, name='groups_list'),
    path('create/', create_group, name='create_group'),
]
