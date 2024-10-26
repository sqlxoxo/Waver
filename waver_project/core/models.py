# core/models.py

from django.contrib.auth.models import AbstractUser
from django.db import models

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