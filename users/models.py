from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):

    # first_name = models.CharField(verbose_name='first_name', max_length=30, null=True, blank=True)
    # last_name =  models.CharField(verbose_name='last_name', max_length=30, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.username = self.email
        return super().save(*args, **kwargs)