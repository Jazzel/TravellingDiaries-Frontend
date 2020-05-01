from rest_framework import serializers
from accounts.api.serializers import UserDisplaySerializer, ProfileModelSerializer
from destinations.api.serializers import DestinationDisplaySerializer
from post.models import Post, PostImage
from django.utils.timesince import timesince
from django.core.files.uploadedfile import InMemoryUploadedFile


class PostImageModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = PostImage
        fields = '__all__'


class PostModelSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        file_fields = kwargs.pop('file_fields', None)
        super().__init__(*args, **kwargs)
        if file_fields:
            field_update_dict = {field: serializers.FileField(
                required=False) for field in file_fields}
            print(field_update_dict)
            print(type(field_update_dict))
            self.fields.update(**field_update_dict)

    def create(self, validated_data):
        validated_data_copy = validated_data.copy()
        validated_files = []
        for key, value in validated_data_copy.items():
            if isinstance(value, InMemoryUploadedFile):
                validated_files.append(value)
                validated_data.pop(key)
        post_instance = super().create(validated_data)
        print(validated_files)
        for file in validated_files:
            PostImage.objects.create(
                post=post_instance, image=file)
        return post_instance

    user = UserDisplaySerializer(read_only=True)
    post_images = PostImageModelSerializer(many=True, read_only=True)
    timesince = serializers.SerializerMethodField()
    destination = DestinationDisplaySerializer(read_only=True)
    did_like = serializers.SerializerMethodField()
    liked = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id', 'user', 'message', 'type',
                  'destination', 'timesince', 'did_like', 'liked', 'post_images']

    def get_timesince(self, obj):
        return timesince(obj.created_at) + " ago"

    def get_did_like(self, obj):
        request = self.context.get("request")
        user = request.user
        if user.is_authenticated:
            if user in obj.liked.all():
                return True
        return False

    def get_liked(self, obj):
        return obj.liked.all().count()
