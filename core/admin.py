from django.contrib import admin
from .models import Menu, Footer, QuickLink, FooterText, PageSection, SectionContent

class MenuAdmin(admin.ModelAdmin):
    list_display = ('text', 'url', 'is_button', 'order', 'is_active')
    search_fields = ('text', 'url')
    list_filter = ('is_active', 'is_button', 'order')
    ordering = ('order',)
    list_editable = ('is_active', 'order', 'is_button')
    fields = ('text', 'url', 'is_button', 'order', 'is_active')

class FooterAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_number', 'address', 'copyright_text')
    search_fields = ('name', 'email')
    fields = ('name', 'email', 'phone_number', 'address', 'image1', 'image2','image3', 'image4', 'facebook_url', 'instagram_url', 'linkedin_url', 'copyright_text')
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

class SectionContentInline(admin.TabularInline):
    model = SectionContent
    extra = 0
    fields = ('title', 'description', 'order', 'instagram_url', 'twitter_url', 'facebook_url', 'image', 'is_active')
    show_change_link = True

class SectionContentAdmin(admin.ModelAdmin):
    list_display = ('title', 'section', 'order', 'is_active')
    search_fields = ('title', 'description')
    list_filter = ('is_active', 'section', 'order')
    ordering = ('order',)
    fields = ('section', 'title', 'description', 'instagram_url', 'twitter_url', 'facebook_url', 'image', 'order', 'is_active')
    readonly_fields = ('section',)

class PageSectionAdmin(admin.ModelAdmin):
    list_display = ['section_type', 'heading', 'order', 'is_active']
    list_filter = ['is_active', 'section_type', 'order']
    search_fields = ['heading', 'subheading', 'super_heading']
    ordering = ['order']

    inlines = [SectionContentInline]

    fieldsets = (
        (None, {
            'fields': ('section_type', 'order', 'is_active', 'heading', 'subheading', 'description')
        }),
        ('Images', {
            'fields': ('background_image', 'primary_image')
        }),
        ('Buttons', {
            'fields': ('primary_button_text', 'primary_button_url', 'secondary_button_text', 'secondary_button_url')
        }),
    )

admin.site.register(PageSection, PageSectionAdmin)
admin.site.register(SectionContent, SectionContentAdmin)
admin.site.register(Menu, MenuAdmin)
admin.site.register(Footer, FooterAdmin)
admin.site.register(QuickLink, QuickLinkAdmin)
admin.site.register(FooterText, FooterTextAdmin)
