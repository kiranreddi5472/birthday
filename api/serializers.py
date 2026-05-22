from rest_framework import serializers
from .models import Wish, Gallery, Dialogue

class WishSerializer(serializers.ModelSerializer):
    # DRF will automatically build a full URL for the image field if a request is active
    class Meta:
        model = Wish
        fields = ['id', 'name', 'message', 'image', 'created_at']
        read_only_fields = ['id', 'created_at']


class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = ['id', 'title', 'image', 'uploaded_at']
        read_only_fields = ['id', 'uploaded_at']


class DialogueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dialogue
        fields = ['id', 'text', 'added_by', 'created_at']
        read_only_fields = ['id', 'created_at']
