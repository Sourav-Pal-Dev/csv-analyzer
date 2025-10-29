from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework import serializers


# -------------------------------------------------
# 1️. Serializer for user registration
# -------------------------------------------------
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=6)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        # Using Django's built-in create_user automatically hashes the password
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email'),
            password=validated_data['password']
        )
        return user


# -------------------------------------------------
# 2️. Serializer for login (credentials validation)
# -------------------------------------------------
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(username=data['username'], password=data['password'])
        if not user:
            raise serializers.ValidationError("Invalid username or password")
        data['user'] = user
        return data


# -------------------------------------------------
# 3️. Serializer for returning safe user info
# -------------------------------------------------
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']
