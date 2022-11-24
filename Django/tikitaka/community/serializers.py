from rest_framework import serializers
from .models import Review, Vote, Comment, Calendar, Message
from movies.models import Movie, Backdrop
from movies.serializers import BackdropSerializer, MovieNameSerializer
from accounts.serializers import UserShortSerializer, UserIdSerializer
from accounts.models import User




class ReviewCreateSerializer(serializers.ModelSerializer):
    # movie = MovieNameSerializer(read_only=True)
    # backdrop = BackdropSerializer(read_only=True)

    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('movie', 'like_users',)


class MessageCreateSerializer(serializers.ModelSerializer):
    # movie = MovieNameSerializer(read_only=True)
    # backdrop = BackdropSerializer(read_only=True)

    class Meta:
        model = Message
        fields = '__all__'
        read_only_fields = ('movie', 'send_at', 'is_checked',)


class CommentSerializer(serializers.ModelSerializer):
    user = UserShortSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('review', 'user')

class ReviewSerializer(serializers.ModelSerializer):
    movie = MovieNameSerializer(read_only=True)
    backdrop = BackdropSerializer(read_only=True)
    user = UserShortSerializer(read_only=True)
    like_users = UserShortSerializer(many=True, read_only=True)
    comment_set = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Review
        fields = '__all__'


class MessageSerializer(serializers.ModelSerializer):
    movie = MovieNameSerializer(read_only=True)
    from_user = UserShortSerializer(read_only=True)
    to_user = UserShortSerializer(read_only=True)

    class Meta:
        model = Message
        fields = '__all__'


class ReviewSerializerForLike(serializers.ModelSerializer):
    movie = MovieNameSerializer(read_only=True)
    backdrop = BackdropSerializer(read_only=True)
    user = UserShortSerializer(read_only=True)
    like_users = UserIdSerializer(many=True, read_only=True)
    comment_set = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Review
        fields = '__all__'


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


class UserMessageSerializer(serializers.ModelSerializer):
    inbox = MessageSerializer(many=True, read_only=True)
    class Meta:
        model = User
        fields = ('inbox',)


class FeedSerializer(serializers.ModelSerializer):
    following = UserReviewSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('following',)