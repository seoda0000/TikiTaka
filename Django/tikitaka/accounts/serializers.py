from rest_framework import serializers
from .models import User
from movies.serializers import PosterSerializer




class UserShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'profile_img', 'email',)

class UserNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email',)

class UserSerializer(serializers.ModelSerializer):
    bookmarks = PosterSerializer(many=True, read_only=True)

    class Meta:
        model = User
        exclude = ('password', 'last_name', 'is_superuser', 'is_staff', 'is_active', 'groups', 'user_permissions',)


class BookmarkSerializer(serializers.ModelSerializer):
    bookmarks = PosterSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('bookmarks',)