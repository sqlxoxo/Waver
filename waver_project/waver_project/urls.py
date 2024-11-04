# waver_project/urls.py

from django.contrib import admin
from django.urls import path, include
from main.views import HomeView  # Ensure HomeView is imported

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('friends/', include('friends.urls')),
    path('messaging/', include('messaging.urls')),
    path('groups/', include('groups.urls')),
    path('', HomeView.as_view(), name='home'),  # Ensure the name is set here
]
