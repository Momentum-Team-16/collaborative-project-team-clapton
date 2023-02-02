from rest_framework import serializers
from .models import User, SocialCard


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'first_name',
            'last_name',
        )


class SocialCardSerializer(serializers.ModelSerializer):
    owner = serializers.SlugRelatedField(slug_field='username', read_only=True)

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
        )
