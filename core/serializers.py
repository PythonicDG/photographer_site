from rest_framework import serializers
from .models import Menu, Footer, QuickLink, FooterText

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
