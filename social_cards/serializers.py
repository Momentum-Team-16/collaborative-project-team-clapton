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
    likes_total = serializers.SerializerMethodField('get_total_likes')
    likes = serializers.SlugRelatedField(slug_field='username', many=True, read_only=True)

    def get_total_likes(self, card):
        return card.likes.count()

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
            'likes',
            'likes_total',
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

class UserAvatarSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('avatar',)

    def update(self, instance, validated_data):
        file = self.initial_data.get("file")
        if file is not None:
            instance.avatar.save(file.name, file)
        return instance