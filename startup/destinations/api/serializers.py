from rest_framework import serializers
from django.urls import reverse_lazy
from destinations.models import Destination


class DestinationDisplaySerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()

    class Meta:
        model = Destination
        fields = [
            'name', 'category'
        ]

    def get_category(self, obj):
        return obj.get_category_display()
