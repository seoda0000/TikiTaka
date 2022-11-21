from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from .managers import CustomUserManager
from movies.models import Movie, Genre


# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=150, blank=True, null=True, unique=True)
    email = models.EmailField(('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()
    profile_img = models.ImageField(upload_to="%Y/%m/%d", null=True, blank=True)
    bookmarks = models.ManyToManyField(Movie, related_name="bookmark_users", blank=True)
    favorite_genres = models.ManyToManyField(Genre, related_name="favorite_users", blank=True)
    description = models.TextField(null=True, blank=True)
    following = models.ManyToManyField('self', symmetrical=False, related_name='follower')
    
    def clean(self):
        if self.username == "":
            self.username = None

    def __str__(self):
        return self.username

class Message(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.PROTECT)
    from_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="outbox")
    to_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="inbox")
    content = models.TextField(null=True, blank=True)
    send_at = models.DateTimeField(auto_now_add=True)
    is_checked = models.BooleanField(default=False)

    








