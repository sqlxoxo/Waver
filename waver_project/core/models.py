from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver


class CustomUser(AbstractUser):
   pass

class UserProfile(models.Model):
   user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
   bio = models.TextField(blank=True)  # Поле для иографии
   location = models.CharField(max_length=30, blank=True)  # Поле для местоположения
   birth_date = models.DateField(null=True, blank=True)  # Поле для даты рождения

   def __str__(self):
      return self.user.username
   
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_profile(sender, instance, created, **kwargs):
   if created:
      UserProfile.objects.create(user=instance)

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def save_user_profile(sender, instance, **kwargs):
   instance.userprofile.save()