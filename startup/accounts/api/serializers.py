from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from accounts.models import UserProfile

User = get_user_model()


class UserDisplaySerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email'
        ]


class ProfileModelSerializer(serializers.ModelSerializer):
    user = UserDisplaySerializer(read_only=True)

    class Meta:
        model = UserProfile
        fields = ['user', 'bio', 'created', 'image']
