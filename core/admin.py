from django.contrib import admin
from .models import Menu, Footer, QuickLink, FooterText


class MenuAdmin(admin.ModelAdmin):
    list_display = ('text', 'url', 'is_button', 'order', 'is_active', 'slug')
    search_fields = ('text', 'url', 'slug')
    list_filter = ('is_active', 'is_button')
    prepopulated_fields = {"slug": ("text",)}
    ordering = ('order',)
    list_editable = ('is_active', 'order', 'is_button')
    fields = ('text', 'url', 'is_button', 'order', 'is_active', 'slug')
    readonly_fields = ('slug',)

class FooterAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_number', 'address', 'copyright_text')
    search_fields = ('name', 'email')
    fields = ('name', 'email', 'phone_number', 'address', 'facebook_url', 'instagram_url', 'linkedin_url', 'copyright_text')
    readonly_fields = ('created_at',)
    ordering = ('name',)

class QuickLinkAdmin(admin.ModelAdmin):
    list_display = ('name', 'url')
    search_fields = ('name', 'url')
    fields = ('name', 'url')

class FooterTextAdmin(admin.ModelAdmin):
    list_display = ('made_with_text',)
    search_fields = ('made_with_text',)
    fields = ('made_with_text',)

admin.site.register(Menu, MenuAdmin)
admin.site.register(Footer, FooterAdmin)
admin.site.register(QuickLink, QuickLinkAdmin)
admin.site.register(FooterText, FooterTextAdmin)
