from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=80)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user.username
