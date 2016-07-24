"""Serializers for pictures."""
from .models import Image

from django.contrib.auth.models import User

from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User

        fields = ('id', 'first_name', 'last_name', 'email')


class ImageSerializer(serializers.ModelSerializer):
    original_image = serializers.ImageField()

    class Meta:
        model = Image

        fields = ('id', 'name', 'uploader', 'original_image', 'edited_image',
                  'date_created', 'date_modified', 'category')

        read_only_fields = ('id', 'name', 'uploader', 'size', 'date_created',
                            'date_modified')
