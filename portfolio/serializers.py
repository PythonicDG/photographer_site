from rest_framework import serializers
from .models import PageSection, SectionContent, Category, AlbumPhoto

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'id', 'name', 'slug', 'view_more_url', 'order'
        ]


class SectionContentSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)

    class Meta:
        model = SectionContent
        fields = [
            'id', 'title', 'description', 'date', 'image', 'order', 'category'
        ]


class PageSectionSerializer(serializers.ModelSerializer):
    content_items = serializers.SerializerMethodField()

    class Meta:
        model = PageSection
        fields = [
            'id', 'section_type', 'order', 'heading', 'subheading',
            'description', 'background_image', 'primary_image',
            'primary_button_text', 'primary_button_url',
            'secondary_button_text', 'secondary_button_url',
            'content_items'
        ]

    def get_content_items(self, obj):
        content_items = obj.content_items.filter(is_active=True).select_related('category')
        return SectionContentSerializer(content_items, many=True).data

class AlbumPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlbumPhoto
        fields = ['id', 'image', 'is_active']


class AlbumCategorySerializer(serializers.ModelSerializer):
    photos = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = [
            'id', 'name', 'slug', 'heading', 'description',
            'cover_image', 'view_more_url', 'order', 'photos'
        ]

    def get_photos(self, obj):
        photos = obj.photos.filter(is_active=True)
        return AlbumPhotoSerializer(photos, many=True).data
