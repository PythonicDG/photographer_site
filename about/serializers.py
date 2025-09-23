from rest_framework import serializers
from .models import PageSection, SectionContent



class SectionContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = SectionContent
        fields = ('id', 'title', 'description', 'image', 'order', 'is_active')

class PageSectionSerializer(serializers.ModelSerializer):
    content_items = SectionContentSerializer(many=True, read_only=True)

    class Meta:
        model = PageSection
        fields = ('id', 'section_type', 'order', 'is_active', 'title', 'heading', 'subheading', 'description', 
                  'background_image', 'primary_image', 'content_items')
