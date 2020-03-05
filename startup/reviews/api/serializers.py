from rest_framework import serializers
from reviews.models import Review
from accounts.api.serializers import UserDisplaySerializer
from destinations.api.serializers import DestinationDisplaySerializer
from django.utils.timesince import timesince


class ReviewModelSerializer(serializers.ModelSerializer):
    user = UserDisplaySerializer(read_only=True)
    destination = DestinationDisplaySerializer(read_only=True)
    destination_rating = serializers.SerializerMethodField()
    destination_type = serializers.SerializerMethodField()

    class Meta:
        model = Review
        fields = [
            'id',
            'user',
            'destination',
            'rating',
            'type',
            'destination_rating',
            'destination_type',
            'comments',
        ]

    def get_destination_rating(self, obj):
        rating_str = obj.get_rating_display()
        return rating_str

    def get_destination_type(self, obj):
        type_str = obj.get_type_display()
        return type_str