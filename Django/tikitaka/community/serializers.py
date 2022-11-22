from rest_framework import serializers
from .models import Review, Vote, Comment, Calendar
from movies.models import Movie, Backdrop
from movies.serializers import BackdropSerializer, MovieNameSerializer
from accounts.serializers import UserShortSerializer
from accounts.models import User



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


class CalendarCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Calendar
        fields = '__all__'

class CalendarSerializer(serializers.ModelSerializer):
    backdrop = BackdropSerializer()
    movie = MovieNameSerializer()

    class Meta:
        model = Calendar
        fields = '__all__'


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

class LikeReviewSerializer(serializers.ModelSerializer):
    like_reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('like_reviews',)



class UserReviewSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)
    class Meta:
        model = User
        fields = ('reviews',)


class UserCalendarSerializer(serializers.ModelSerializer):
    calendar_set = CalendarSerializer(many=True, read_only=True)
    class Meta:
        model = User
        fields = ('calendar_set',)

class FeedSerializer(serializers.ModelSerializer):
    following = UserReviewSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('following',)