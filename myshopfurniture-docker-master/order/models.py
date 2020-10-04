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

from product.models import *
from customer.models import *
from order.models import *


from django.contrib.auth.models import User

from django import forms
from django.forms import ModelForm



class Order(models.Model):
	user = models.ForeignKey(User, null=True, blank=True, verbose_name="Utente")
	code = models.CharField('Codice', max_length=250, null=True, blank=True)
	tot_price = models.DecimalField('Prezzo', max_digits=10, decimal_places=2, blank=True, null=True, default=0)
	pub_date = models.DateTimeField('date published', editable=False)
	inlavorazione = models.BooleanField('in lavorazione', default=False)
	pagato = models.BooleanField('pagato', default=False)
	spedito = models.BooleanField('spedito', default=False)
	chiuso = models.BooleanField('chiuso', default=False)

	def ivato(self):
		iva = self.tot_price * 22/100
		ivato = self.tot_price + iva
		return ivato

	def save(self, *args, **kwargs):
		self.pub_date = datetime.now()
		super(Order, self).save(*args, **kwargs) # Call the "real" save() method.

	def __unicode__(self):
		return self.pub_date.strftime('%Y-%m-%d')

	class Meta:
		verbose_name_plural = "Ordine"
		ordering = ['id']




class OrderItem(models.Model):
	order = models.ForeignKey(Order, null=True, blank=True, verbose_name="Ordine")
	product = models.ForeignKey(Product, null=True, blank=True, verbose_name="Prodotto")
	#prezzo
	price = models.DecimalField('Prezzo', max_digits=10, decimal_places=2, blank=True, null=True)
	price_total = models.DecimalField('Prezzo', max_digits=10, decimal_places=2, blank=True, null=True)
	quantity = models.IntegerField(blank=True, null=True, verbose_name="quantita")
	pub_date = models.DateTimeField('date published', editable=False)

	def save(self, *args, **kwargs):
		self.pub_date = datetime.now()
		self.price_total = self.price * self.quantity ## ok ok ok 
		super(OrderItem, self).save(*args, **kwargs) # Call the "real" save() method.

	def __unicode__(self):
		return self.pub_date.strftime('%Y-%m-%d')

	class Meta:
		verbose_name_plural = "Prodotti in Ordine"
		ordering = ['id']




class AddOrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['user', 'tot_price']



class AddOrderItemForm(ModelForm):
	class Meta:
		model = OrderItem
		fields = ['order', 'product', 'quantity', 'price', 'price_total']



##### PERSONALIZZA ################
class Personalizza(models.Model):
	#user = models.ForeignKey(User, null=True, blank=True, verbose_name="Utente")
	product = models.ForeignKey(Product, null=True, blank=True, verbose_name="Prodotto")
	metriq = models.IntegerField(blank=True, null=True, verbose_name="Metri Quadri Locale")
	email_user = models.CharField('email user', max_length=250, null=True, blank=True)
	user_indirizzo = models.TextField('indirizzo', null=True, blank=True)
	pub_date = models.DateTimeField('date published', editable=False)
	inlavorazione = models.BooleanField('in lavorazione', default=False)
	chiuso = models.BooleanField('chiuso', default=False)

	def save(self, *args, **kwargs):
		self.pub_date = datetime.now()
		super(Personalizza, self).save(*args, **kwargs) # Call the "real" save() method.

	def __unicode__(self):
		return self.pub_date.strftime('%Y-%m-%d')

	class Meta:
		verbose_name_plural = "Personalizzazione"
		ordering = ['id']



class PersonalizzaItem(models.Model):
	personalizza = models.ForeignKey(Personalizza, null=True, blank=True, verbose_name="Personalizza")
	moduli = models.ForeignKey(Moduli, null=True, blank=True, verbose_name="Moduli")
	#prezzo
	quantity = models.IntegerField(blank=True, null=True, verbose_name="quantita")
	pub_date = models.DateTimeField('date published', editable=False)

	def save(self, *args, **kwargs):
		self.pub_date = datetime.now()
		super(PersonalizzaItem, self).save(*args, **kwargs) # Call the "real" save() method.

	def __unicode__(self):
		return self.pub_date.strftime('%Y-%m-%d')

	class Meta:
		verbose_name_plural = "Personalizzazione Item"
		ordering = ['id']



class AddPersonalizzaForm(ModelForm):
    class Meta:
        model = Personalizza
        fields = ['product', 'metriq', 'email_user', 'user_indirizzo']



class PersonalizzaItemForm(ModelForm):
	class Meta:
		model = PersonalizzaItem
		fields = ['personalizza', 'moduli', 'quantity']

