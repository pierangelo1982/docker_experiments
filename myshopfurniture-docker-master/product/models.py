#!/usr/bin/env python
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
#from product.forms import *
from django.utils.timezone import datetime

from django import forms

import django_filters



class Gallery(models.Model):
    title = models.CharField(max_length=100, verbose_name="Titolo del Progetto:")
    image = models.ImageField(blank=True, null=True, upload_to='slider_product', verbose_name="Immagine")
    slider = ImageRatioField('image', '1000x556', verbose_name="Slider")
    thumb = ImageRatioField('image', '800x578', verbose_name="Miniatura")
    thumbdue = ImageRatioField('image', '745x558', verbose_name="Miniatura pagina dettaglio")
    croplibero = ImageRatioField('image', '595x335', free_crop=True, verbose_name="Ritaglio Libero")
    pub_date = models.DateTimeField('date published')

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
        verbose_name_plural = "Galleria Immagini"
        ordering = ['id']


class Category(models.Model):
    title = models.CharField('titolo', max_length=100)
    title_uk = models.CharField('Titolo Inglese', max_length=250, null=True, blank=True)
    subtitle = models.CharField('sottotitolo', max_length=250, null=True, blank=True)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Categorie"




class Color(models.Model):
    category = models.ForeignKey(Category, null=True, blank=True, verbose_name="Seleziona Categoria")
    name = models.CharField('nome colore', max_length=100)
    code = models.CharField('codice colore', max_length=250, null=True, blank=True)
    css_color = models.CharField('css colore', max_length=250, null=True, blank=True)
    image = models.ImageField('immagine colore', blank=True, null=True, upload_to='color')
    thumb = ImageRatioField('image', '300x150', verbose_name="Miniatura: 300x150px")

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Colori"




class Material(models.Model):
    name = models.CharField('nome colore', max_length=100)
    image = models.ImageField('immagine colore', blank=True, null=True, upload_to='color')
    description = models.TextField('descrizione', null=True, blank=True)
    thumb = ImageRatioField('image', '300x300', verbose_name="Miniatura")
    price = models.DecimalField('Prezzo', max_digits=10, decimal_places=2, blank=True, null=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Materiali"



class Video(models.Model):
    category = models.ForeignKey(Category, null=True, blank=True, verbose_name="Seleziona Categoria")
    title = models.CharField('titolo', max_length=100)
    code = models.CharField('codice youtube', max_length=250, null=True, blank=True)
    url = models.CharField('url youtube', max_length=250, null=True, blank=True)
    frame = models.TextField(null=True, blank=True, verbose_name="Frame embedded youtube")
    image = models.ImageField('immagine colore', blank=True, null=True, upload_to='color')
    thumb = ImageRatioField('image', '300x150', verbose_name="Miniatura: 300x150px")
    active = models.BooleanField('attiva', default=False)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Video"




class Accessory(models.Model):
    name = models.CharField(max_length=100, verbose_name="Titolo:")
    code = models.CharField('Codice', max_length=250, null=True, blank=True)
    category = models.ManyToManyField(Category, null=True, blank=True, verbose_name="Seleziona Categorie")
    ##PRICE
    price = models.DecimalField('Prezzo', max_digits=10, decimal_places=2, blank=True, null=True)
    discount = models.IntegerField(blank=True, null=True, verbose_name="sconto percentuale")
    price_offer = models.DecimalField('Prezzo Scontato', max_digits=10, decimal_places=2, blank=True, null=True)
    ##MULTIMEDIA
    image = models.ImageField(blank=True, null=True, upload_to='accessory', verbose_name="Immagine")
    slider = ImageRatioField('image', '1170x600', verbose_name="Slider")
    thumb = ImageRatioField('image', '800x578', verbose_name="Miniatura")
    thumbdue = ImageRatioField('image', '745x558', verbose_name="Miniatura pagina dettaglio")
    croplibero = ImageRatioField('image', '595x335', free_crop=True, verbose_name="Ritaglio Libero")
    album = FilerFolderField(null=True, blank=True)
    ## Composition
    color = models.ManyToManyField(Color, null=True, blank=True, verbose_name="Seleziona Colori")
    material = models.ManyToManyField(Material, null=True, blank=True, verbose_name="Seleziona Materiali")
    ## Data
    quantity = models.IntegerField(blank=True, null=True, verbose_name="Quantita")
    size = models.CharField('Misure', max_length=250, null=True, blank=True)
    width = models.IntegerField(blank=True, null=True, verbose_name="larghezza")
    lenght = models.IntegerField(blank=True, null=True, verbose_name="lunghezza")
    depth = models.IntegerField(blank=True, null=True, verbose_name="Profondita")
    height = models.IntegerField(blank=True, null=True, verbose_name="altezza")
    volume = models.DecimalField('Volume', max_digits=10, decimal_places=2, blank=True, null=True)
    descrizione = models.TextField(null=True, blank=True, verbose_name="Descrizione")
    allegato = models.FileField(blank=True, null=True, upload_to='allegato')
    ## Delivery
    prompt_delivery = models.BooleanField('Pronta Consegna', default=False)
    delivery = models.BooleanField('Consegna 40gg', default=False)
    tags = TaggableManager(verbose_name="Parole chiave", blank=True)
    pub_date = models.DateTimeField('date published')
    active = models.BooleanField('attiva', default=False)
    slide = models.BooleanField('Mostra in Slide', default=False)
    promo = models.BooleanField('Mostra in Promo', default=False)



    def image_img(self):
        if self.image:
            return u'<img src="%s" style="width:300px"/>' % self.image.url
        else:
            return '(Sin imagen)'
    image_img.short_description = 'Thumb'
    image_img.allow_tags = True

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Accessori"
        ordering = ['id']




class Moduli(models.Model):
    name = models.CharField(max_length=100, verbose_name="Titolo:")
    name_uk = models.CharField('Titolo Inglese', max_length=250, null=True, blank=True)
    code = models.CharField('Codice', max_length=250, null=True, blank=True)
    category = models.ManyToManyField(Category, null=True, blank=True, verbose_name="Seleziona Categorie")
    ## composizione
    quantity = models.IntegerField(blank=True, null=True, verbose_name="quantita",
                                    help_text = "quantita quando non e composizione")
    ##PRICE
    price = models.DecimalField('Prezzo', max_digits=10, decimal_places=2, blank=True, null=True,
                                help_text = "prezzo base")
    discount = models.IntegerField(blank=True, null=True, default= 0, verbose_name="sconto percentuale")
    price_offer = models.DecimalField('Prezzo Scontato', max_digits=10, decimal_places=2, blank=True, null=True)
    ##MULTIMEDIA
    image = models.ImageField(blank=True, null=True, upload_to='product', verbose_name="Immagine")
    slider = ImageRatioField('image', '1000x556', verbose_name="Slider")
    thumb = ImageRatioField('image', '800x578', verbose_name="Miniatura")
    thumbdue = ImageRatioField('image', '745x558', verbose_name="Miniatura pagina dettaglio")
    croplibero = ImageRatioField('image', '595x335', free_crop=True, verbose_name="Ritaglio Libero")
    album = FilerFolderField(null=True, blank=True)
    video = models.ManyToManyField(Video, null=True, blank=True, verbose_name="Video")
    ## Data
    color = models.ManyToManyField(Color, null=True, blank=True, verbose_name="Seleziona Colori",
                                    help_text="solo se a 40 giorni")
    material = models.ManyToManyField(Material, null=True, blank=True, verbose_name="Seleziona Materiale")
    size = models.CharField('Misure', max_length=250, null=True, blank=True)
    width = models.IntegerField(blank=True, null=True, verbose_name="larghezza")
    lenght = models.IntegerField(blank=True, null=True, verbose_name="lunghezza")
    depth = models.IntegerField(blank=True, null=True, verbose_name="Profondita")
    height = models.IntegerField(blank=True, null=True, verbose_name="altezza")
    volume = models.DecimalField('Volume', max_digits=10, decimal_places=2, blank=True, null=True)
    descrizione = models.TextField(null=True, blank=True, verbose_name="Descrizione")
    descrizione_uk = models.TextField(null=True, blank=True, verbose_name="Descrizione Inglese")
    allegato = models.FileField(blank=True, null=True, upload_to='allegato')
    ## Accessory
    tags = TaggableManager(verbose_name="Parole chiave", blank=True)
    pub_date = models.DateTimeField('date published', editable=False)
    active = models.BooleanField('attiva', default=False)
    slide = models.BooleanField('Mostra in Slide', default=False)
    promo = models.BooleanField('Mostra in Promo', default=False)

    def save(self, *args, **kwargs):
        self.price_offer = self.price - (self.price * self.discount/100)
        self.pub_date = datetime.now()
        super(Moduli, self).save(*args, **kwargs) # Call the "real" save() method.

    def image_img(self):
        if self.image:
            return u'<img src="%s" style="width:300px"/>' % self.image.url
        else:
            return '(Sin imagen)'
    image_img.short_description = 'Thumb'
    image_img.allow_tags = True

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Moduli"
        ordering = ['id']





class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="Titolo:")
    name_uk = models.CharField('Titolo Inglese', max_length=250, null=True, blank=True)
    code = models.CharField('Codice', max_length=250, null=True, blank=True)
    category = models.ManyToManyField(Category, null=True, blank=True, verbose_name="Seleziona Categorie")
    ## composizione
    quantity = models.IntegerField(blank=True, null=True, verbose_name="quantita",
                                    help_text = "quantita quando non e composizione")
    ##PRICE
    price = models.DecimalField('Prezzo', max_digits=10, decimal_places=2, blank=True, null=True,
                                help_text = "prezzo base")
    discount = models.IntegerField(blank=True, null=True, default= 0, verbose_name="sconto percentuale")
    price_offer = models.DecimalField('Prezzo Scontato', max_digits=10, decimal_places=2, blank=True, null=True)
    ##MULTIMEDIA
    image = models.ImageField(blank=True, null=True, upload_to='product', verbose_name="Immagine")
    gallery = models.ManyToManyField(Gallery, null=True, blank=True, verbose_name="Seleziona Immagini x Slider")
    slider = ImageRatioField('image', '1000x556', verbose_name="Slider")
    thumb = ImageRatioField('image', '800x578', verbose_name="Miniatura")
    thumbdue = ImageRatioField('image', '745x558', verbose_name="Miniatura pagina dettaglio")
    croplibero = ImageRatioField('image', '595x335', free_crop=True, verbose_name="Ritaglio Libero")
    album = FilerFolderField(null=True, blank=True)
    video = models.ManyToManyField(Video, null=True, blank=True, verbose_name="Video")
    ## Data
    color = models.ManyToManyField(Color, null=True, blank=True, verbose_name="Seleziona Colori",
                                    help_text="solo se a 40 giorni")
    material = models.ManyToManyField(Material, null=True, blank=True, verbose_name="Seleziona Materiale")
    size = models.CharField('Misure', max_length=250, null=True, blank=True)
    width = models.IntegerField(blank=True, null=True, verbose_name="larghezza")
    lenght = models.IntegerField(blank=True, null=True, verbose_name="lunghezza")
    depth = models.IntegerField(blank=True, null=True, verbose_name="Profondita")
    height = models.IntegerField(blank=True, null=True, verbose_name="altezza")
    volume = models.DecimalField('Volume', max_digits=10, decimal_places=2, blank=True, null=True)
    descrizione = models.TextField(null=True, blank=True, verbose_name="Descrizione")
    descrizione_uk = models.TextField(null=True, blank=True, verbose_name="Descrizione Inglese")
    allegato = models.FileField(blank=True, null=True, upload_to='allegato')
    moduli = models.ManyToManyField(Moduli, null=True, blank=True, verbose_name="Seleziona Moduli")
    ## Accessory
    tags = TaggableManager(verbose_name="Parole chiave", blank=True)
    pub_date = models.DateTimeField('date published', editable=False)
    active = models.BooleanField('attiva', default=False)
    slide = models.BooleanField('Mostra in Slide', default=False)
    promo = models.BooleanField('Mostra in Promo', default=False)

    def ivato(self):
        iva = self.price * 22/100
        ivato = self.price + iva
        return ivato

    def save(self, *args, **kwargs):
        self.price_offer = self.price - (self.price * self.discount/100)
        self.pub_date = datetime.now()
        super(Product, self).save(*args, **kwargs) # Call the "real" save() method.

    def image_img(self):
        if self.image:
            return u'<img src="%s" style="width:300px"/>' % self.image.url
        else:
            return '(Sin imagen)'
    image_img.short_description = 'Thumb'
    image_img.allow_tags = True

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Prodotti"
        ordering = ['id']





class Composition(models.Model):
    product = models.ForeignKey(Product, null=True, blank=True, verbose_name="Prodotto")
    modulo = models.ForeignKey(Moduli, null=True, blank=True, verbose_name="Modulo")
    name = models.CharField(max_length=100, verbose_name="Titolo:", null=True, editable=False)
    code = models.CharField('Codice', max_length=250, null=True, blank=True, editable=False)
    price = models.DecimalField('Prezzo', max_digits=10, decimal_places=2, blank=True, null=True, default= 0,
                                help_text = "maggiorazione di prezzo")
    image = models.ImageField(blank=True, null=True, upload_to='product', verbose_name="Immagine")
    slider = ImageRatioField('image', '1000x556', verbose_name="Slider")
    thumb = ImageRatioField('image', '800x578', verbose_name="Miniatura")
    thumbdue = ImageRatioField('image', '745x558', verbose_name="Miniatura pagina dettaglio")
    video = models.ManyToManyField(Video, null=True, blank=True, verbose_name="Video")
    croplibero = ImageRatioField('image', '595x335', free_crop=True, verbose_name="Ritaglio Libero")
    color = models.ForeignKey(Color, null=True, blank=True, verbose_name="Colori")
    material = models.ForeignKey(Material, null=True, blank=True, verbose_name="Metallo", editable=False)
    ## Data
    quantity = models.IntegerField(blank=True, null=True, verbose_name="quantita")
    allegato = models.FileField(blank=True, null=True, upload_to='allegato')
    pub_date = models.DateTimeField('date published', editable=False)
    active = models.BooleanField('attiva', default=False)

    def image_img(self):
        if self.image:
            return u'<img src="%s" style="width:300px"/>' % self.image.url
        else:
            return '(Sin imagen)'
    image_img.short_description = 'Thumb'
    image_img.allow_tags = True

    def save(self, *args, **kwargs):
        self.name = self.product.name + self.modulo.name
        self.code = self.product.id + self.modulo.id
        self.price = (self.modulo.price * self.quantity)
        self.pub_date = datetime.now()
        super(Composition, self).save(*args, **kwargs) # Call the "real" save() method.

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Componente"
        ordering = ['id']





## FILTER
class ProductFilter(django_filters.FilterSet):
    #name = django_filters.CharFilter(lookup_expr='iexact')
    price = django_filters.NumberFilter()
    price__gt = django_filters.NumberFilter(name='price', lookup_expr='gt')
    price__lt = django_filters.NumberFilter(name='price', lookup_expr='lt')

    class Meta:
        model = Product
        fields = ['price', 'pub_date']




## forms
class ProductForm(forms.Form):
    product = Product.objects.first
    nome = forms.CharField(label='Nome', max_length=100)
    quantity = forms.IntegerField(label='Quantita')
    color = forms.ModelChoiceField(queryset=Color.objects.all().order_by('-id'))
    material = forms.ModelChoiceField(queryset=Material.objects.all().order_by('-id'))




