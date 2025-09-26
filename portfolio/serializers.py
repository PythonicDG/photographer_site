from rest_framework import serializers
from .models import PageSection, SectionContent, Album, AlbumPhoto


class SectionContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = SectionContent
        fields = ('id', 'category', 'title', 'description', 'date', 'image', 'order', 'is_active')


class PageSectionSerializer(serializers.ModelSerializer):
    content_items = SectionContentSerializer(many=True, read_only=True)

    class Meta:
        model = PageSection
        fields = (
            'id', 'section_type', 'order', 'is_active',
            'heading', 'subheading', 'description',
            'background_image', 'primary_image',
            'primary_button_text', 'primary_button_url',
            'secondary_button_text', 'secondary_button_url',
            'content_items'
        )

class AlbumPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlbumPhoto
        fields = ['id', 'image', 'is_active']

class AlbumSerializer(serializers.ModelSerializer):
    photos = AlbumPhotoSerializer(many=True, read_only=True)

    class Meta:
        model = Album
        fields = ['id', 'name', 'slug', 'heading', 'description', 'cover_image', 'order', 'is_active', 'photos']
