from rest_framework import serializers
from .models import User, SocialCard
from taggit.serializers import TagListSerializerField, TaggitSerializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'first_name',
            'last_name',
        )


class SocialCardSerializer(serializers.ModelSerializer, TaggitSerializer):
    owner = serializers.SlugRelatedField(slug_field='username', read_only=True)
    tags = TagListSerializerField()

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
            'border_color',
            'tags'
        )
