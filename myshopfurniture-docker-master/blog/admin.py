from django.contrib import admin
from blog.models import *
from image_cropping import ImageCroppingMixin

# Register your models here.
class MyModelAdmin(ImageCroppingMixin, admin.ModelAdmin):
    pass


class BlogAdmin(ImageCroppingMixin, admin.ModelAdmin):
    list_display = ("image_img", "name", "active")



admin.site.register(Blog, MyModelAdmin)
