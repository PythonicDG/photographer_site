import os
import io
from PIL import Image as PilImage
from django.core.files.base import ContentFile
from django.db import models

class PageSection(models.Model):
    SECTION_TYPES = [
        ('HERO', 'Hero Banner'),
        ('GALLERY', 'Gallery'),
        ('WHO_YOU_ARE', 'Who You Are'),
        ('ACHIEVEMENTS', 'Achievements'),
    ]

    section_type = models.CharField(max_length = 50, choices = SECTION_TYPES)
    order = models.PositiveIntegerField(default = 0)
    is_active = models.BooleanField(default = True)
    
    title = models.CharField(max_length = 255, blank = True, null = True)
    heading = models.CharField(max_length = 255, blank = True, null = True)
    subheading = models.CharField(max_length = 255, blank = True, null = True)
    description = models.TextField(blank = True, null = True)

    background_image = models.ImageField(upload_to = 'sections/', blank = True, null = True)
    primary_image = models.ImageField(upload_to = 'sections/', blank = True, null = True)


    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.get_section_type_display()}"

    def save(self, *args, **kwargs):
        def convert_to_webp(image_field):
            if image_field and hasattr(image_field, 'file'):
                image = PilImage.open(image_field.file)
                image_io = io.BytesIO()
                image.save(image_io, format = 'WEBP', quality = 85)
                image_io.seek(0)
                file_name = os.path.splitext(os.path.basename(image_field.name))[0]
                new_file_name = f"{file_name}.webp"
                image_field.save(new_file_name, ContentFile(image_io.read()), save = False)

        convert_to_webp(self.background_image)
        convert_to_webp(self.primary_image)

        super().save(*args, **kwargs)


class SectionContent(models.Model):
    section = models.ForeignKey(PageSection, related_name = 'content_items', on_delete = models.CASCADE)
    order = models.PositiveIntegerField(default = 0)
    is_active = models.BooleanField(default = True)

    title = models.CharField(max_length = 200, blank = True, null = True)
    description = models.TextField(blank = True, null = True)
    image = models.ImageField(upload_to = 'images/', blank = True, null = True)

    class Meta:
        ordering = ['section', 'order']

    def __str__(self):
        return self.title or f"Content Item #{self.id}"

    def save(self, *args, **kwargs):
        def convert_to_webp(image_field):
            if image_field and hasattr(image_field, 'file'):
                image = PilImage.open(image_field.file)
                image_io = io.BytesIO()
                image.save(image_io, format = 'WEBP', quality = 85)
                image_io.seek(0)
                file_name = os.path.splitext(os.path.basename(image_field.name))[0]
                new_file_name = f"{file_name}.webp"
                image_field.save(new_file_name, ContentFile(image_io.read()), save = False)

        convert_to_webp(self.image)

        super().save(*args, **kwargs)
