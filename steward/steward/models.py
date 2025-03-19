from django.db import models
from django.contrib.auth.models import User
from django.apps import AppConfig

class StewardConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'steward'  # Ensure this matches your app folder name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    workplace = models.CharField(max_length=100)
    role = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
