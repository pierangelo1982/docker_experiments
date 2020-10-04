from django.conf.urls import include, url, patterns
from django.contrib import admin
from sito import views
from sito.views import *
from blog.views import *
from django.conf import settings
from django.conf.urls.static import static
from sito.forms import LoginForm
import importlib

from django.views.generic import TemplateView




urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    url(r'^$', HomePage, name='home'),
    url(r'^demo/$', DemoHomePage, name='home-demo'),
    url(r'^(?P<language>[a-z\-]+)/product/(?P<post_id>\d+)/$', views.ProductFilterView, name='detail'),
    url(r'^(?P<language>[a-z\-]+)/category/(?P<post_id>\d+)/$', views.ProductFilterCategory, name='categoria'),
    # personalizzazione
    url(r'^(?P<language>[a-z\-]+)/personalizzazione/(?P<post_id>\d+)/$', views.Personalizzazione, name='personalizzazione'),
    url(r'^add-personalizzazione/$', views.add_personalizzazione, name='personalizzazione-add'),
    # richiesta
    url(r'^richiesta/$', views.add_richiesta, name='richiesta'),
    #cart
    url(r'^add-to-cart/$', views.add, name='add-to-cart'),
    url(r'^show-cart/$', views.show, name='show-cart'),
    url(r'^remove-cart/(?P<post_id>\d+)/$', views.remove, name='remove-cart'),
    #order
    url(r'^addorder/$', views.add_to_order, name='add-order'),
    url(r'^order/$', views.order, name='order'),
    url(r'^order/(?P<post_id>\d+)/$', views.orderDetail, name='order-detail'),
    # customer
    url(r'^customer/$', views.customer_page, name='customer'),
    url(r'^add_fatturazionecustomer/$', views.add_customer_fatturazione, name='add-fatturazione'),
    url(r'^add_indirizzo_spedizione/$', views.add_customer_indirizzo_spedizione, name='add-indirizzo-spedizione'),
    url(r'^update_fatturazionecustomer/(?P<pk>\d+)/$', views.update_customer_fatturazione, name='update-fatturazione'),
    url(r'^update_indirizzo_spedizione/(?P<pk>\d+)/$', views.update_customer_indirizzo_spedizione, name='update-indirizzo-spedizione'),
    ## cerca
    url(r'^results/$', views.search, name="risultati"),
    ## video
    url(r'^(?P<language>[a-z\-]+)/video/$', views.video, name='video'),
    ## page
    url(r'^(?P<language>[a-z\-]+)/page/(?P<post_id>\d+)/$', views.PageDetail, name='pagina-dettaglio'),
    url(r'^(?P<language>[a-z\-]+)/finiture/$', views.finiture, name='finiture'),
    ## blog
    url(r'^(?P<language>[a-z\-]+)/blog/$', blogView, name='blog'),
    url(r'^(?P<language>[a-z\-]+)/blog/(?P<post_id>\d+)/$', blogDetail, name='blog-dettaglio'),
    #login
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^register/$', views.register_user_page, name="registra-utente"),
    url(r'^add-user/$', views.add_user, name="add-user"),
    ## pagine statiche
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^contact-home/$', views.contactHome, name='contact-home'),
    url(r'^add-newsletter/$', views.add_newsletter, name='add-newsletter'),
    url(r'^sitemap\.xml$', TemplateView.as_view(template_name='sitemap.xml', content_type='text/xml')),
    url(r'^robots\.txt$', TemplateView.as_view(template_name='robots.txt', content_type='text/xml')),
    url(r'^language/(?P<language>[a-z\-]+)/$', views.language),
    ## edit language ###################
    url(r'^product/(?P<post_id>\d+)/$', views.ProductFilterViewdue, name='detail-lang'),
    url(r'^category/(?P<post_id>\d+)/$', views.ProductFilterCategorydue, name='categoria-lang'),
    url(r'^video/$', views.videodue, name='video-lang'),
    ## page
    url(r'^page/(?P<post_id>\d+)/$', views.PageDetaildue, name='pagina-dettaglio-lang'),
    url(r'^finiture/$', views.finituredue, name='finiture-lang'),
    ## blog
    url(r'^blog/$', blogViewdue, name='blog-lang'),
    url(r'^blog/(?P<post_id>\d+)/$', blogDetaildue, name='blog-dettaglio-lang'),
   ]
