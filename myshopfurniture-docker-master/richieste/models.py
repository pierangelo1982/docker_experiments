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
from django.forms import ModelForm

from filer.fields.image import FilerImageField
from filer.fields.file import FilerFileField

# Create your models here.

class Richiesta(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Titolo")
    cognome = models.CharField(max_length=100, verbose_name="cognome")
    indirizzo = models.CharField(max_length=100, blank=True, null=True, verbose_name="indirizzo")
    civico = models.CharField(max_length=100, blank=True, null=True, verbose_name="numero civico")
    cap = models.CharField(max_length=100, blank=True, null=True, verbose_name="cap")
    citta = models.CharField(max_length=100, blank=True, null=True, verbose_name="citta")
    telefono = models.CharField(max_length=100, blank=True, null=True, verbose_name="telefono")
    email = models.CharField(max_length=100, blank=True, null=True, verbose_name="email")
    oggetto = models.CharField(max_length=100, blank=True, null=True, verbose_name="oggetto")
    descrizione = models.TextField(null=True, blank=True, verbose_name="Descrizione")
    allegato = models.FileField(blank=True, null=True, upload_to='richieste_allegati')
    pub_date = models.DateTimeField('date published')

    def __unicode__(self):
        return str(self.pub_date)

    class Meta:
        verbose_name_plural = "Richiesta"
        ordering = ['-id']



class RichiestaForm(ModelForm):
    class Meta:
        model = Richiesta
        fields = ['nome', 'cognome', 'indirizzo', 'civico', 'cap', 'citta', 'telefono', 'email', 'oggetto', 'descrizione', 'allegato']

