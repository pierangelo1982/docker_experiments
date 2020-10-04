from django.contrib import admin
from order.models import *
from image_cropping import ImageCroppingMixin

from nested_inline.admin import NestedStackedInline, NestedModelAdmin


# Register your models here.
class MyModelAdmin(ImageCroppingMixin, admin.ModelAdmin):
    pass


######## ORDER ##############################
class OrderListItemAdmin(NestedStackedInline):
    model = OrderItem
    extra = 2
    fk_name = 'order'
    list_display = ("quantity", "price", "price_total")
    fields = (
        ("order", "product", "quantity"),
        ("price_total")
        )



class OrderAdmin(ImageCroppingMixin, admin.ModelAdmin):
    list_display = ("user", "code", "tot_price", "inlavorazione", "pagato", "spedito", "chiuso")
    list_editable=("inlavorazione", "pagato", "spedito", "chiuso")
    fields = (
        ("user", "code"),
        ("tot_price"),
        ("inlavorazione", "pagato", "spedito", "chiuso")
        )
    model = Order
    inlines = [OrderListItemAdmin]

    
class OrderItemAdmin(ImageCroppingMixin, admin.ModelAdmin):
    list_display = ("quantity", "price", "price_total")


############ PERSONALIZZAZIONE ###########################
class PersonalizzaListItemAdmin(NestedStackedInline):
    model = PersonalizzaItem
    extra = 2
    fk_name = 'personalizza'
    list_display = ("pub_date", "moduli", "quantity")
    fields = ('personalizza', 'moduli', 'quantity')


class PersonalizzaAdmin(ImageCroppingMixin, admin.ModelAdmin):
    list_display = ("email_user", "product", "metriq")
    fields = ('email_user', 'product', 'metriq')
    model = Personalizza
    inlines = [PersonalizzaListItemAdmin]

    
class PersItemAdmin(ImageCroppingMixin, admin.ModelAdmin):
    list_display = ("personalizza", "pub_date", "quantity")

admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(Order, OrderAdmin)

admin.site.register(PersonalizzaItem, PersItemAdmin)
admin.site.register(Personalizza, PersonalizzaAdmin)

#
