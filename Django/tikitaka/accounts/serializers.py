from rest_framework import serializers
from .models import User




class UserShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'profile_img', 'email',)

