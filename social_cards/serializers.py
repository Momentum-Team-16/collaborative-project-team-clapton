from rest_framework import serializers
from .models import User, SocialCard, Follower, Comments
from taggit.serializers import TagListSerializerField, TaggitSerializer


class UserSerializer(serializers.ModelSerializer):
    followed_list = serializers.CharField()

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'first_name',
            'last_name',
            'followed_list',
        )


class SocialCardSerializer(TaggitSerializer, serializers.ModelSerializer):
    owner = serializers.SlugRelatedField(slug_field='username', read_only=True)
    tags = TagListSerializerField(read_only=True)

    class Meta:
        model = SocialCard
        fields = (
            'id',
            'owner',
            'title',
            'front_message',
            'back_message',
            'front_image',
            'back_image',
            'font',
            'text_color',
            'text_align',
            'border_color',
            'border_style',
            'tags',
        )


class FollowerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Follower
        fields = ('id', 'user', 'followed', 'created')

class CommentsSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = Comments
        fields = ('id', 'social_card', 'comment', 'user')
