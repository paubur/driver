from django.contrib.auth.models import User
from rest_framework import serializers

from forum.models import ForumPost, ForumPostAnswer


class ForumPostSerializer(serializers.ModelSerializer):
    # user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = ForumPost
        fields = ['id', 'title', 'description', 'user']


class ForumPostAnswerSerializer(serializers.ModelSerializer):
    # user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = ForumPostAnswer
        fields = ['id', 'description', 'forumpost', 'user']

