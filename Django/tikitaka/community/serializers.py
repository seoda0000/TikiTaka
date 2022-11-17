from rest_framework import serializers
from .models import Review, Vote, Comment
from movies.models import Movie, Backdrop
from movies.serializers import BackdropSerializer, MovieNameSerializer
from accounts.serializers import UserShortSerializer



class ReviewSerializer(serializers.ModelSerializer):
    movie = MovieNameSerializer(read_only=True)
    backdrop = BackdropSerializer(read_only=True)
    user = UserShortSerializer(read_only=True)

    class Meta:
        model = Review
        fields = '__all__'


class ReviewCreateSerializer(serializers.ModelSerializer):
    movie = MovieNameSerializer(read_only=True)
    # backdrop = BackdropSerializer(read_only=True)

    class Meta:
        model = Review
        fields = '__all__'