from rest_framework import serializers
from accounts.api.serializers import UserDisplaySerializer, ProfileModelSerializer
from destinations.api.serializers import DestinationDisplaySerializer
from post.models import Post, PostImage
from django.utils.timesince import timesince


class PostImageModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = PostImage
        fields = ['image']


class PostModelSerializer(serializers.ModelSerializer):
    user = UserDisplaySerializer(read_only=True)
    post_images = PostImageModelSerializer(many=True, read_only=True)
    timesince = serializers.SerializerMethodField()
    destination = DestinationDisplaySerializer(read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'user', 'message',
                  'destination', 'timesince', 'post_images']

    def get_timesince(self, obj):
        return timesince(obj.created_at) + " ago"
