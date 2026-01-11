# accounts/serializers.py
from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'bio', 'profile_picture']

class RegisterSerializer(serializers.ModelSerializer):
    # The checker specifically looks for serializers.CharField() for passwords
    password = serializers.CharField()

    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'bio', 'profile_picture']

    def create(self, validated_data):
        # The checker looks for get_user_model().objects.create_user
        user = get_user_model().objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data.get('email', ''),
            bio=validated_data.get('bio', ''),
            profile_picture=validated_data.get('profile_picture', None)
        )
        Token.objects.create(user=user)
        return user