import os
import io
from PIL import Image as PilImage
from django.core.files.base import ContentFile
from django.db import models
from django.utils.text import slugify

class PageSection(models.Model):
    SECTION_TYPES = [
        ('HERO', 'Hero Banner'),
        ('GALLERY', 'Gallery'),
        ('SHOWCASE', 'Showcase'),
        ('SECTION_4', 'Section 4'),
        ('SECTION_5', 'Section 5'),
    ]

    section_type = models.CharField(max_length=50, choices=SECTION_TYPES)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    heading = models.CharField(max_length=255, blank=True, null=True)
    subheading = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    background_image = models.ImageField(upload_to='sections/', blank=True, null=True)
    primary_image = models.ImageField(upload_to='sections/', blank=True, null=True)

    primary_button_text = models.CharField(max_length=50, blank=True, null=True)
    primary_button_url = models.CharField(max_length=200, blank=True, null=True)

    secondary_button_text = models.CharField(max_length=50, blank=True, null=True)
    secondary_button_url = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.get_section_type_display()} - {self.heading or 'Untitled'}"

    def save(self, *args, **kwargs):
        def convert_to_webp(image_field):
            if image_field and hasattr(image_field, 'file'):
                image = PilImage.open(image_field.file)
                image_io = io.BytesIO()
                image.save(image_io, format='WEBP', quality=85)
                image_io.seek(0)
                file_name = os.path.splitext(os.path.basename(image_field.name))[0]
                new_file_name = f"{file_name}.webp"
                image_field.save(new_file_name, ContentFile(image_io.read()), save=False)

        convert_to_webp(self.background_image)
        convert_to_webp(self.primary_image)
        super().save(*args, **kwargs)


class SectionContent(models.Model):
    CATEGORY_CHOICES = [
        ('PORTRAITS', 'Portraits Photography'),
        ('EVENTS', 'Events Photography'),
        ('COMMERCIAL', 'Commercial Photography'),
    ]

    section = models.ForeignKey(PageSection, related_name='content_items', on_delete=models.CASCADE)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, blank=True, null=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    title = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    date = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.get_category_display() if self.category else ''} {self.title or f'Item #{self.id}'}"

    def save(self, *args, **kwargs):
        def convert_to_webp(image_field):
            if image_field and hasattr(image_field, 'file'):
                image = PilImage.open(image_field.file)
                image_io = io.BytesIO()
                image.save(image_io, format='WEBP', quality=85)
                image_io.seek(0)
                file_name = os.path.splitext(os.path.basename(image_field.name))[0]
                new_file_name = f"{file_name}.webp"
                image_field.save(new_file_name, ContentFile(image_io.read()), save=False)

        convert_to_webp(self.image)
        super().save(*args, **kwargs)


class Album(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length = 100, unique = True, blank = True)
    heading = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    cover_image = models.ImageField(upload_to='albums/', blank=True, null=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)

        def convert_to_webp(image_field):
            if image_field and hasattr(image_field, 'file'):
                image = PilImage.open(image_field.file)
                image_io = io.BytesIO()
                image.save(image_io, format='WEBP', quality=85)
                image_io.seek(0)
                file_name = os.path.splitext(os.path.basename(image_field.name))[0]
                new_file_name = f"{file_name}.webp"
                image_field.save(new_file_name, ContentFile(image_io.read()), save=False)

        convert_to_webp(self.cover_image)
        super().save(*args, **kwargs)


class AlbumPhoto(models.Model):
    album = models.ForeignKey(Album, related_name='photos', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='album_photos/')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"Photo #{self.id}"

    def save(self, *args, **kwargs):
        def convert_to_webp(image_field):
            if image_field and hasattr(image_field, 'file'):
                image = PilImage.open(image_field.file)
                image_io = io.BytesIO()
                image.save(image_io, format='WEBP', quality=85)
                image_io.seek(0)
                file_name = os.path.splitext(os.path.basename(image_field.name))[0]
                new_file_name = f"{file_name}.webp"
                image_field.save(new_file_name, ContentFile(image_io.read()), save=False)

        convert_to_webp(self.image)
        super().save(*args, **kwargs)
