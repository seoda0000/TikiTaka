from django.db import models
from django.contrib.postgres.fields import ArrayField 

# Create your models here.
class Genre(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    name = models.CharField(max_length=50)


class Movie(models.Model):
    adult = models.BooleanField()
    backdrop_path = models.CharField(max_length=100)
    genres = models.ManyToManyField(Genre, related_name="movies")
    id = models.IntegerField(unique=True, primary_key=True)
    original_title = models.CharField(max_length=100)
    overview = models.TextField()
    popularity = models.FloatField()
    poster_path = models.CharField(max_length=200)
    release_date = models.DateField()
    title = models.CharField(max_length=100)
    video = models.BooleanField()
    vote_average = models.FloatField()
    vote_count = models.IntegerField()
