from rest_framework import serializers
from .models import Menu, Footer, QuickLink, FooterText, PageSection, SectionContent

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ('id', 'text', 'url', 'is_button', 'order', 'is_active')


class FooterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Footer
        fields = (
            'id', 'name', 'email', 'phone_number', 'address', 
            'facebook_url', 'instagram_url', 'linkedin_url', 'copyright_text'
        )

class QuickLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuickLink
        fields = ('name', 'url')

class FooterTextSerializer(serializers.ModelSerializer):
    class Meta:
        model = FooterText
        fields = ('made_with_text',)

class HeaderFooterSerializer(serializers.Serializer):
    menus = MenuSerializer(many=True)
    footer = FooterSerializer()
    
    quick_links = QuickLinkSerializer(many=True)
    made_with_text = FooterTextSerializer()


class SectionContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = SectionContent
        fields = ('id', 'title', 'description', 'instagram_url', 'twitter_url', 'facebook_url', 'image', 'order', 'is_active')

class PageSectionSerializer(serializers.ModelSerializer):
    content_items = SectionContentSerializer(many=True, read_only=True)

    class Meta:
        model = PageSection
        fields = ('id', 'section_type', 'order', 'is_active', 'heading', 'subheading', 'description', 
                  'background_image', 'primary_image', 'primary_button_text', 'primary_button_url', 
                  'secondary_button_text', 'secondary_button_url', 'content_items')
