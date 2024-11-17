from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)

    def clean(self):
        if self.email and not self.email.endswith('@example.com'):
            raise ValidationError('Please use a valid email address.')

    def __str__(self):
        return self.username
