import os
import io
from PIL import Image as PilImage
from django.core.files.base import ContentFile
from django.db import models

class Menu(models.Model):
    text = models.CharField(max_length = 100)
    url = models.CharField(max_length = 200, blank = True, null = True)
    is_button = models.BooleanField(default = False)
    order = models.PositiveIntegerField(default = 0)
    is_active = models.BooleanField(default = True)

    def __str__(self):
        return self.text


class Footer(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    
    facebook_url = models.URLField(blank=True, null=True)
    instagram_url = models.URLField(blank=True, null=True)
    linkedin_url = models.URLField(blank=True, null=True)

    copyright_text = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class QuickLink(models.Model):
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class FooterText(models.Model):
    made_with_text = models.CharField(max_length=255)

    def __str__(self):
        return self.made_with_text