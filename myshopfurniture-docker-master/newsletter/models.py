from __future__ import unicode_literals
from django.db import models
from taggit.managers import TaggableManager
from tinymce.models import HTMLField
from django.utils import timezone
from datetime import datetime, timedelta, time, date
#from product.forms import *

from django.contrib.auth.models import User

from django import forms
from django.forms import ModelForm
# Create your models here.

class Newsletter(models.Model):
	newsletter_email = models.CharField('email', max_length=250, null=True, blank=True)
	pub_date = models.DateTimeField('date published', editable=True)

	def save(self, *args, **kwargs):
		self.pub_date = datetime.now()
		super(Newsletter, self).save(*args, **kwargs) # Call the "real" save() method.

	def __unicode__(self):
		return self.newsletter_email

	class Meta:
		verbose_name_plural = "Newsletter"
		ordering = ['-pub_date']



class NewsletterForm(ModelForm):
    class Meta:
        model = Newsletter
        fields = ['newsletter_email']
