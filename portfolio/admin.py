from django.contrib import admin
from .models import PageSection, SectionContent, Album, AlbumPhoto


class SectionContentInline(admin.TabularInline):
    model = SectionContent
    extra = 1
    fields = ('title', 'category', 'description', 'order', 'image', 'is_active')
    show_change_link = True


@admin.register(PageSection)
class PageSectionAdmin(admin.ModelAdmin):
    list_display = ['section_type', 'heading', 'order', 'is_active']
    list_filter = ['section_type', 'is_active']
    search_fields = ['heading', 'subheading']
    ordering = ['order']
    inlines = [SectionContentInline]

    fieldsets = (
        (None, {'fields': ('section_type', 'order', 'is_active', 'heading', 'subheading', 'description')}),
        ('Images', {'fields': ('background_image', 'primary_image')}),
        ('Buttons', {'fields': ('primary_button_text', 'primary_button_url', 
                                'secondary_button_text', 'secondary_button_url')}),
    )


@admin.register(SectionContent)
class SectionContentAdmin(admin.ModelAdmin):
    list_display = ('title', 'section', 'order', 'is_active')
    list_filter = ('section', 'is_active')
    search_fields = ('title', 'description')
    ordering = ('order',)


class AlbumPhotoInline(admin.TabularInline):
    model = AlbumPhoto
    extra = 1
    fields = ('image', 'is_active')
    show_change_link = True

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ['name', 'heading', 'order', 'is_active']
    list_filter = ['is_active']
    search_fields = ['name', 'heading', 'description']
    ordering = ['order']
    inlines = [AlbumPhotoInline]

    fieldsets = (
        (None, {'fields': ('name', 'heading', 'description','slug', 'order', 'is_active')}),
        ('Cover Image', {'fields': ('cover_image',)}),
    )

@admin.register(AlbumPhoto)
class AlbumPhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'album', 'is_active')
    list_filter = ('album', 'is_active')
    ordering = ('album', 'id')