from rest_framework import serializers

from api.models import Image
from api.models import Thumbnails


class ImageSerializer(serializers.ModelSerializer):
    """Image Model Serializer. """

    class Meta:
        model = Image
        fields = ('id', 'name', 'uploader', 'original_image',
                  'date_created', 'date_modified', 'category')
        read_only_fields = ('id', 'name', 'uploader', 'size', 'date_created',
                            'date_modified')


class ThumbnailsSerializer(serializers.ModelSerializer):
    """Thumbnails Model Serializer."""

    class Meta:
        model = Thumbnails
        fields = ('id', 'name', 'original_image',
                  'effect', 'date_created', 'date_modified')
        read_only_fields = ('id', 'name', 'effect', 'original_image',
                            'date_created', 'date_modified')
