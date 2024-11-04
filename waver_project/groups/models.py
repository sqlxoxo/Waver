# groups/models.py
from django.db import models
from django.conf import settings

class Group(models.Model):
    name = models.CharField(max_length=100)
    members = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='group_memberships')  # Измените 'groups' на 'group_memberships'

    def __str__(self):
        return self.name
