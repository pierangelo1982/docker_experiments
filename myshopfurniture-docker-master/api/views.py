# coding=utf-8
from django.shortcuts import render
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.views.generic import ListView, DetailView
from django.template.loader import render_to_string
from product.models import *
from product.forms import *
from sito.models import *
from order.models import *
from blog.models import *
from newsletter.models import *
from richieste.models import *
from django.core.mail import send_mail
from filer.models import *
# cart
from carton.cart import Cart
#login
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

from django.shortcuts import redirect

from django.db.models import Sum
from decimal import *
from decimal import Decimal

from django.core.mail import EmailMultiAlternatives

from django.contrib import messages

import datetime

from django.db.models import Q

from sito.helper import *

from django.core import serializers


#from somewhere import handle_uploaded_file
# Create your views here.

def api_moduli(request):
	moduli_list = Moduli.objects.all().order_by('name')
	data = serializers.serialize("json", moduli_list)
	return HttpResponse(data, content_type='application/json;')  


def api_negozi(request):
	negozi_list = Product.objects.all()
	data = serializers.serialize("json", negozi_list)
	return HttpResponse(data, content_type='application/json;') 

def api_composizioni(request):
	comp_list = Composition.objects.all()
	data = serializers.serialize("json", comp_list)
	return HttpResponse(data, content_type='application/json;')


	## creo arreo negozi
	## dentro classe con composition ottengo un array dei id moduli presenti nel negozio
	
