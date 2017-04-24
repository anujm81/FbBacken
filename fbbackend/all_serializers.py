from django.contrib.auth.models import User
from rest_framework import serializers

from fbbackend.models import UserProfile, Messages, Comments


class MsgSerializer(serializers.Serializer):
    message = serializers.CharField(max_length=4000)


class FriendSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('profile_pic','cover_pic', 'about', 'intro')

class UserSerializer(serializers.ModelSerializer):
    userprofile = FriendSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'userprofile')


class MsgSerializer(serializers.ModelSerializer):
    class Meta:
        model = Messages
        fields = ('message', 'created')

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ('comment', 'created')