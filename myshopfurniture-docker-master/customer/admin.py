# coding=utf-8

from django.contrib import admin
from customer.models import *
from django.forms import CheckboxSelectMultiple

#import nested_admin
from nested_inline.admin import NestedStackedInline, NestedModelAdmin

from django.contrib.auth.models import User


# Register your models here.

def get_username(self):
    return self.user.username


class UserAdmin(admin.ModelAdmin):
	pass

class CustomerAdmin(admin.ModelAdmin):
    list_display = (get_username, "discount", "active")
    model = User
    extra = 1
    fk_name = 'user'

class FatturazioneAdmin(admin.ModelAdmin):
    list_display = (get_username, "denominazione", "piva", "codfisc", "telefono", "e_mail")
    fields = (
        ("user", "denominazione"),
        ("piva", "codfisc"),
        "indirizzo",
        ("cap", "citta", "nazione"),
        ("telefono", "fax"),
        ("e_mail", "pec"),
        "indirizzo_spedizione"
    )

class IndirizzoSpedizioneAdmin(admin.ModelAdmin):
    list_display = (get_username, "spedizione_denominazione",  "spedizione_telefono", "spedizione_e_mail")
    fields = (
        ("user", "spedizione_denominazione"),
        "spedizione_indirizzo",
        ("spedizione_cap", "spedizione_citta", "spedizione_nazione"),
        ("spedizione_telefono", "spedizione_fax"),
        "spedizione_e_mail"
    )


    
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Fatturazione, FatturazioneAdmin)
admin.site.register(IndirizzoSpedizione, IndirizzoSpedizioneAdmin)
