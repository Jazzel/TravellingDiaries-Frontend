from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from accounts.models import UserProfile

User = get_user_model()


class UserDisplaySerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'url',
        ]

    def get_url(self, obj):
        return reverse_lazy("user_profile", kwargs={'username': obj.username})


class ProfileModelSerializer(serializers.ModelSerializer):
    user = UserDisplaySerializer(read_only=True)

    class Meta:
        model = UserProfile
        fields = ['user', 'bio', 'created', 'image']
