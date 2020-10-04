from django.contrib import admin
from product.models import *
from image_cropping import ImageCroppingMixin
from django.forms import CheckboxSelectMultiple

#import nested_admin
from nested_inline.admin import NestedStackedInline, NestedModelAdmin




def get_category(self):
    return self.category.title

def get_product(self):
	return self.product.name

def get_color(self):
    return self.color.name

def get_material(self):
    return self.material.name

def get_modulo(self):
    return self.modulo.name


class MyModelAdmin(ImageCroppingMixin, admin.ModelAdmin):
    pass


class VideoAdmin(admin.ModelAdmin):
    list_display = ("title", "code", "url", "active")
 

class AccessoryAdmin(ImageCroppingMixin, admin.ModelAdmin):
    list_display = ("image_img", "code", "name", "price", "discount", "price_offer", "promo", "active") 


class CompositionAdmin(ImageCroppingMixin, admin.ModelAdmin):
    list_display = ("code", get_modulo, "image_img", "name", "price", "active")
    #fields = ('image', 'name', 'quantity')


class ColorAdmin(ImageCroppingMixin, admin.ModelAdmin):
	list_display = ("category", "name")


class GalleryAdmin(ImageCroppingMixin, admin.ModelAdmin):
    list_display = ("image_img", "title")



                   
class CompositionAssociactionAdmin(NestedStackedInline):
    model = Composition
    extra = 1
    fk_name = 'product'
    fields = (('modulo', 'image'), ('color', 'quantity'))



class ProductAdmin(ImageCroppingMixin, admin.ModelAdmin):
    #duplicate function
    def duplicate_event(ModelAdmin, request, queryset):
        for object in queryset:
            object.id = None
            object.save()
    duplicate_event.short_description = "Duplica Record Selezionati"
    save_as = True

    model = Product
    inlines = [CompositionAssociactionAdmin]
    list_display = ("image_img", "code", "name", "price", "discount", "price_offer",  "promo", "active")
    list_editable = ('active',)
    fields = (
                "code",
                ("name", "name_uk"),
                "category", 
                ("price", "discount"),
                "quantity",
                "color",
                "size",
                ("width", "lenght", "depth", "height"),
                "volume",
                "allegato",
                "descrizione", "descrizione_uk",
                 "album",
                 "video",
                 "moduli",
                "image", "slider", "thumb", "thumbdue", "croplibero", "gallery",
                ("slide", "promo"),
                "tags", "active"
            )

    actions = ['duplicate_event']
    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }



class ModuliAdmin(ImageCroppingMixin, admin.ModelAdmin):
    #duplicate function
    def duplicate_event(ModelAdmin, request, queryset):
        for object in queryset:
            object.id = None
            object.save()
    duplicate_event.short_description = "Duplica Record Selezionati"
    save_as = True

    list_display = ("image_img", "code", "name", "price", "discount", "price_offer",  "promo", "active")
    list_editable = ('active',)
    fields = (
                "code",
                ("name", "name_uk"),
                "category", 
                ("price", "discount"),
                "quantity",
                "color",
                "size",
                ("width", "lenght", "depth", "height"),
                "volume",
                "allegato",
                "descrizione", "descrizione_uk",
                 "album",
                "image", "slider", "thumb", "thumbdue", "croplibero",
                ("slide", "promo"),
                "tags", "active"
            )

    actions = ['duplicate_event']





admin.site.register(Category, MyModelAdmin)
admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Color, ColorAdmin)
admin.site.register(Material, MyModelAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Composition, CompositionAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(Moduli, ModuliAdmin)






