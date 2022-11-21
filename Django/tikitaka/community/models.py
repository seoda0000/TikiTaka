from django.db import models
from django.conf import settings
from movies.models import Movie, Backdrop

# Create your models here.
class Vote(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="like_reviews")
    content = models.CharField(max_length=200)
    movie = models.ForeignKey(Movie, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_recommended = models.BooleanField()


class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="like_reviews")
    title = models.CharField(max_length=100)
    movie = models.ForeignKey(Movie, on_delete=models.PROTECT)
    backdrop = models.ForeignKey(Backdrop, on_delete=models.PROTECT)
    content = models.TextField()
    # viewing_date = models.DateField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # is_public = models.BooleanField


class Comment(models.Model):
    content = models.TextField()
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Calendar(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.PROTECT)
    backdrop = models.ForeignKey(Backdrop, on_delete=models.PROTECT)
    start = models.DateField()
