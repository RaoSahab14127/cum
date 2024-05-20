from django.contrib.auth.models import AbstractUser
from django.db import models

from .managers import UserManager

class CustomUser(AbstractUser):
    username = None
    phone_number = models.CharField(max_length=100,unique=True)

    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = []
    objects = UserManager()