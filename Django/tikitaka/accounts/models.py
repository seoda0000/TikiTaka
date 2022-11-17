from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

from .managers import CustomUserManager


# Create your models here.
class User(AbstractUser):
    username = None
    email = models.EmailField(('email address'), unique=True)
    nickname = models.CharField(max_length=100, null=True, default=None)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    

    def __str__(self):
        return self.email

