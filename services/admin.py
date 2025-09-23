from django.contrib import admin
from .models import PageSection, SectionContent


class SectionContentInline(admin.TabularInline):
    model = SectionContent
    extra = 0
    fields = ('title', 'image', 'order', 'is_active')
    show_change_link = True

class SectionContentAdmin(admin.ModelAdmin):
    list_display = ('title', 'section', 'order', 'is_active')
    search_fields = ('title',)
    list_filter = ('is_active', 'section', 'order')
    ordering = ('order',)
    fields = ('section', 'title', 'image', 'order', 'is_active')
    readonly_fields = ('section',)

class PageSectionAdmin(admin.ModelAdmin):
    list_display = ['section_type', 'heading', 'order', 'is_active']
    list_filter = ['is_active', 'section_type', 'order']
    search_fields = ['heading',]
    ordering = ['order']

    inlines = [SectionContentInline]

    fieldsets = (
        (None, {
            'fields': ('section_type', 'order', 'is_active', 'heading', 'description')
        }),
        ('Images', {
            'fields': ('primary_image',)
        }),
        ('Buttons', {
            'fields': ('primary_button_text', 'primary_button_url', 'secondary_button_text', 'secondary_button_url')
        }),
    )

admin.site.register(PageSection, PageSectionAdmin)
admin.site.register(SectionContent, SectionContentAdmin)
