from __future__ import unicode_literals
from django.db import models
from image_cropping import ImageRatioField, ImageCropField
from datetime import datetime, timedelta, time, date
from django.utils.timesince import timesince
from filer.fields.image import FilerImageField
from filer.fields.file import FilerFileField
from filer.fields.folder import FilerFolderField
from taggit.managers import TaggableManager
from tinymce.models import HTMLField
from django.utils import timezone
from django import forms

from product.models import *

from filer.fields.image import FilerImageField
from filer.fields.file import FilerFileField

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=100, verbose_name="Titolo")
    title_uk = models.CharField(max_length=100, verbose_name="Titolo UK")
    image = models.ImageField(blank=True, null=True, upload_to='slider')
    body = models.TextField(null=True, blank=True, verbose_name="Descrizione")
    body_uk = models.TextField(null=True, blank=True, verbose_name="Descrizione UK")
    link = models.TextField(null=True, blank=True)
    slider = ImageRatioField('image', '1000x300', verbose_name="Gallery in Home")
    video = models.TextField(null=True, blank=True, verbose_name="Video")
    album = FilerFolderField(null=True, blank=True)
    pub_date = models.DateTimeField('date published')
    active = models.BooleanField('attiva',
                                    default=False)
    chiavi = models.TextField(null=True, blank=True, verbose_name="Parole Chiave")

    def image_img(self):
        if self.image:
            return u'<img src="%s" style="width:300px"/>' % self.image.url
        else:
            return '(Sin imagen)'
    image_img.short_description = 'Thumb'
    image_img.allow_tags = True

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Blog"
        ordering = ['id']
