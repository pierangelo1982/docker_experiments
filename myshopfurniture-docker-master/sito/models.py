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




class Slider(models.Model):
    category = models.ForeignKey(Category, null=True, blank=True, verbose_name="Seleziona Categoria")
    name = models.CharField(max_length=100, verbose_name="Titolo")
    image = models.ImageField(blank=True, null=True, upload_to='slider')
    scritta = models.TextField(null=True, blank=True)
    body = models.TextField(null=True, blank=True)
    link = models.TextField(null=True, blank=True)
    slider = ImageRatioField('image', '1000x556', verbose_name="Gallery in Home")
    pub_date = models.DateTimeField('date published')
    active = models.BooleanField('attiva',
                                    default=False)

    def image_img(self):
        if self.image:
            return u'<img src="%s" style="width:300px"/>' % self.image.url
        else:
            return '(Sin imagen)'
    image_img.short_description = 'Thumb'
    image_img.allow_tags = True

    def __unicode__(self):
        return self.titolo

    class Meta:
        verbose_name_plural = "Slider"
        ordering = ['id']



class Page(models.Model):
    title = models.CharField(max_length=100, verbose_name="Titolo")
    title_uk = models.CharField(max_length=100, verbose_name="Titolo UK")
    image = models.ImageField(blank=True, null=True, upload_to='slider')
    body = models.TextField(null=True, blank=True, verbose_name="Descrizione")
    body_uk = models.TextField(null=True, blank=True, verbose_name="Descrizione UK")
    link = models.TextField(null=True, blank=True)
    slider = ImageRatioField('image', '1000x300', verbose_name="Gallery in Home")
    album = FilerFolderField(null=True, blank=True)
    pub_date = models.DateTimeField('date published')
    active = models.BooleanField('attiva',
                                    default=False)

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
        verbose_name_plural = "Pagine"
        ordering = ['id']




class ContactForm(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100)
    cognome = forms.CharField(label='Cognome', max_length=100)
    telefono = forms.CharField(label='Telefono', max_length=100, required = False)
    fax = forms.CharField(label='Fax', max_length=100, required = False)
    email = forms.CharField(label='email', max_length=100)
    web = forms.CharField(label='Web', max_length=100, required = False)
    indirizzo = forms.CharField(label='Indirizzo', max_length=100, required = False)
    civico = forms.CharField(label='Civico', max_length=100, required = False)
    citta = forms.CharField(label='Citta', max_length=100, required = False)
    cap = forms.CharField(label='CAP', max_length=100, required = False)
    oggetto = forms.CharField(label='Oggetto', max_length=100, required = False)
    messaggio = forms.CharField(label='Messaggio', widget=forms.Textarea, required = False)




class ContactFormHome(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100)
    cognome = forms.CharField(label='Cognome', max_length=100)
    telefono = forms.CharField(label='Telefono', max_length=100, required = False)
    email = forms.CharField(label='email', max_length=100)
    web = forms.CharField(label='Web', max_length=100, required = False)
    indirizzo = forms.CharField(label='Indirizzo', max_length=100, required = False)
    civico = forms.CharField(label='Civico', max_length=100, required = False)
    citta = forms.CharField(label='Citta', max_length=100, required = False)
    cap = forms.CharField(label='CAP', max_length=100, required = False)
    oggetto = forms.CharField(label='Oggetto', max_length=100, required = False)
    messaggio = forms.CharField(label='Messaggio', widget=forms.Textarea, required = False)