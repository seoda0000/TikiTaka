from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

from .managers import CustomUserManager
from movies.models import Movie


# Create your models here.
class User(AbstractUser):
    username = None
    email = models.EmailField(('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()
    profile_img = models.ImageField(upload_to="%Y/%m/%d", null=True, blank=True)
    bookmarks = models.ManyToManyField(Movie, related_name="bookmark_users")

    

    def __str__(self):
        return self.email





