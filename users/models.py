from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    name = models.OneToOneField(User, on_delete=models.CASCADE, max_length=50)
    bio = models.TextField(blank=True)
