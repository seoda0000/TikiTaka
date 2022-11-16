from django.db import models
from django.contrib.postgres.fields import ArrayField 

# Create your models here.

class Country(models.Model):
    iso_3166_1 = models.CharField(max_length=10, unique=True, primary_key=True)
    english_name = models.CharField(max_length=50)
    native_name = models.CharField(max_length=50)


class Genre(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    name = models.CharField(max_length=50)


class WatchProvider(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    name = models.CharField(max_length=50)
    logo_path = models.CharField(max_length=200)


class People(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    profile_path = models.CharField(max_length=200, null=True)
    name_origin = models.CharField(max_length=100, null=True)
    


class Movie(models.Model):
    # 기본 항목
    adult = models.BooleanField(null=True)
    backdrop_path = models.CharField(max_length=100, null=True)
    genres = models.ManyToManyField(Genre, related_name="movies")
    id = models.IntegerField(unique=True, primary_key=True)
    original_title = models.CharField(max_length=100, null=True)
    overview = models.TextField(null=True)
    popularity = models.FloatField(null=True)
    poster_path = models.CharField(max_length=200, null=True)
    release_date = models.DateField(null=True)
    title = models.CharField(max_length=100, null=True)
    video = models.BooleanField(null=True)
    vote_average = models.FloatField(null=True)
    vote_count = models.IntegerField(null=True)

    # 디테일 항목
    runtime = models.IntegerField(null=True)
    status = models.CharField(max_length=100, null=True)
    countries = models.ManyToManyField(Country, related_name="movies")

    # Watch_Provider 항목
    watch_providers = models.ManyToManyField(WatchProvider, related_name="movies")

    # people 항목
    casts = models.ManyToManyField(People, related_name="movies")
    director = models.ForeignKey(People, null=True, on_delete=models.SET_NULL)


