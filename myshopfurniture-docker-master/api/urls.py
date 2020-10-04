from django.conf.urls import include, url, patterns
from django.contrib import admin
from api import views
from api.views import *
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    url(r'^moduli/$', api_moduli, name='api-moduli'),
    url(r'^negozi/$', api_negozi, name='api-negozi'),
    url(r'^composizioni/$', api_composizioni, name='api-composizioni'),
   ]
   