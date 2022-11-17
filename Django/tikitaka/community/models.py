from django.db import models
from django.conf import settings

# Create your models here.
# class Review(models.Model):
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="like_reviews")
    # title = models.CharField(max_length=100)
    # movie_title = models.CharField(max_length=50)
    # rank = models.IntegerField()
    # content = models.TextField()
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)


# class Comment(models.Model):
    # content = models.TextField()
    # review = models.ForeignKey(Review, on_delete=models.CASCADE)
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
