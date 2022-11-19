from rest_framework import serializers
from .models import Movie, Country, People, WatchProvider, Genre, Backdrop



class BackdropSerializer(serializers.ModelSerializer):

    class Meta:
        model = Backdrop
        fields = ('id', 'path',)


class PosterListSerializer(serializers.ModelSerializer):
    backdrop_set = BackdropSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = ('id', 'title', 'original_title', 'poster_path', 'backdrop_set',)


class MovieNameSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('title',)


# class ReviewListSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Review
#         fields = ('title', 'content',)


# class ReviewSerializer(serializers.ModelSerializer):
#     movie = MovieNameSerializer(read_only=True)

#     class Meta:
#         model = Review
#         fields = '__all__'


# class ActorListSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Actor
#         fields = '__all__'
#         read_only_fields = ('movies',)

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class WatchProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = WatchProvider
        fields = '__all__'


class PeopleShortSerializer(serializers.ModelSerializer):

    class Meta:
        model = People
        fields = ('name', 'profile_path',)


class MovieDetailSerializer(serializers.ModelSerializer):
    backdrop_set = BackdropSerializer(many=True, read_only=True)
    director = PeopleShortSerializer(read_only=True)
    casts = PeopleShortSerializer(many=True, read_only=True)
    watch_providers = WatchProviderSerializer(many=True, read_only=True)
    genres = GenreSerializer(many=True, read_only=True)
    class Meta:
        model = Movie
        fields = '__all__'




class PeopleSerializer(serializers.ModelSerializer):
    movies = PosterListSerializer(many=True, read_only=True)
    class Meta:
        model = People
        fields = '__all__'
