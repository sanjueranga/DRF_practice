from django.contrib.auth.models import User
from rest_framework import serializers
from .models import UserProfile

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'first_name', 'last_name', 'password']

    extra_kwargs = {
        'password': {'write_only': True},  
    }

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
        )
        return user

class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    is_email_confirmed = serializers.BooleanField()

    class Meta:
        model = UserProfile
        fields = ['user', 'is_email_confirmed']