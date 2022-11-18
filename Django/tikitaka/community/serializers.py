from rest_framework import serializers
from .models import Review, Vote, Comment
from movies.models import Movie, Backdrop
from movies.serializers import BackdropSerializer, MovieNameSerializer
from accounts.serializers import UserShortSerializer



class ReviewSerializer(serializers.ModelSerializer):
    movie = MovieNameSerializer(read_only=True)
    backdrop = BackdropSerializer(read_only=True)
    user = UserShortSerializer(read_only=True)
    like_user = UserShortSerializer(read_only=True)

    class Meta:
        model = Review
        fields = '__all__'


class ReviewCreateSerializer(serializers.ModelSerializer):
    # movie = MovieNameSerializer(read_only=True)
    # backdrop = BackdropSerializer(read_only=True)

    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('movie', 'like_users',)


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('review', 'user')


class CommentCreateSerializer(serializers.ModelSerializer):
    # review = ReviewSerializer(read_only=True)
    # backdrop = BackdropSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('review',)


class VoteSerializer(serializers.ModelSerializer):


    class Meta:
        model = Vote
        fields = '__all__'
        read_only_fields = ('movie', 'user')


class VoteCreateSerializer(serializers.ModelSerializer):
    # review = ReviewSerializer(read_only=True)
    # backdrop = BackdropSerializer(read_only=True)

    class Meta:
        model = Vote
        fields = '__all__'
        read_only_fields = ('movie',)