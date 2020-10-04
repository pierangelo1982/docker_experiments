from django.contrib import admin

from richieste.models import *
from image_cropping import ImageCroppingMixin
from django.forms import CheckboxSelectMultiple

#import nested_admin
from nested_inline.admin import NestedStackedInline, NestedModelAdmin

# Register your models here.
class MyModelAdmin(ImageCroppingMixin, admin.ModelAdmin):
    pass


class RichiesteAdmin(admin.ModelAdmin):
    list_display = ("pub_date", "nome", "cognome", "oggetto", "allegato")


admin.site.register(Richiesta, RichiesteAdmin)

