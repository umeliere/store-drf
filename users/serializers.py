from django.contrib.auth import get_user_model
from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import serializers

User = get_user_model()

# thank you https://github.com/sunscrapers/djoser for the code


class CustomUserSerializer(UserSerializer):
    """
    Overridden serializer for detail-user
    """
    class Meta:
        model = User
        fields = ("id", "first_name", "last_name", "username", "phone", "email", "photo", "address", "city")
        read_only_fields = ("username",)


class CustomUserCreateSerializer(UserCreateSerializer):
    """
    Overridden serializer for registration
    """
    password = serializers.CharField(style={"input_type": "password"}, write_only=True, label='Пароль')

    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id', 'username', "phone", 'email', 'password',)
