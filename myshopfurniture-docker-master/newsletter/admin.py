from django.contrib import admin
from newsletter.models import *
from image_cropping import ImageCroppingMixin



# Register your models here.
class MyModelAdmin(ImageCroppingMixin, admin.ModelAdmin):
    pass

# Register your models here.

admin.site.register(Newsletter, MyModelAdmin)

