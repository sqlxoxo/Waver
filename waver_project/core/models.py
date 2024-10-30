# core/models.py

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

class CustomUser(AbstractUser):
   """Пользовательская модель пользователя, наследуемая от AbstractUser."""
   email = models.EmailField(unique=True)

class UserProfile(models.Model):
   """Модель профиля пользователя."""
   user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
   bio = models.TextField(blank=True, null=True)
   profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)

   def __str__(self):
      return f'{self.user.username} Profile'
   
class FriendRequest(models.Model):
   from_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='sent_requests', on_delete=models.CASCADE)
   to_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='received_requests', on_delete=models.CASCADE)
   status = models.CharField(max_length=10, choices=[('pending', 'Pending'), ('accepted', 'Accepted'), ('rejected', 'Rejected')], default='pending')
   created_at = models.DateTimeField(auto_now_add=True)
   