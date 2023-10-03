from rest_framework import serializers
from . models import Feed


class GETFeedSerializer(serializers.ModelSerializer):

    class Meta:
        model = Feed
        read_only_fields=("id","created")
        fields = [
            "id", "headline", "description",
            "poster", "created", "source", "feed_type",
            "image_url",
        ]

class POSTFeedSerializer(serializers.ModelSerializer):

    class Meta:
        model = Feed
        read_only_fields=("id","created")
        fields = [
            "id", "headline", "description",
            "poster", "created", "source", "feed_type",
            "image_url",
        ]
