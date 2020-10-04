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

#from somewhere import handle_uploaded_file





#@login_required(login_url="/login/")
def HomePage(request):
    slider_list = Slider.objects.filter(active=True).order_by('id')
    video_list = Video.objects.filter(active=True).order_by('id')
    product_list = Product.objects.all().order_by('?')
    blog_list = Blog.objects.all().order_by('-pub_date')[:4]
    context = {'slider_list':slider_list,
                'video_list':video_list,
                'product_list':product_list,
                'blog_list': blog_list}
    return render_to_response('index.html', context, context_instance=RequestContext(request))



def DemoHomePage(request):
    slider_list = Slider.objects.filter(active=True).order_by('id')
    video_list = Video.objects.filter(active=True).order_by('id')
    product_list = Product.objects.all().order_by('?')
    blog_list = Blog.objects.all().order_by('-pub_date')[:4]
    moduli_list = Moduli.objects.all().order_by('?')
    context = {'slider_list':slider_list,
                'video_list':video_list,
                'product_list':product_list,
                'blog_list': blog_list,
                'moduli_list':moduli_list}
    return render_to_response('index_demo.html', context, context_instance=RequestContext(request))



#@login_required(login_url="/login/")
def ProductFilterCategory(request, post_id, language):
    product_list = Product.objects.filter(category__in=post_id)
    category = Category.objects.get(pk=post_id)
    video_list = Video.objects.filter(active=True).filter(category_id=post_id).order_by('id')
    context = {'product_list': product_list,
                'category':category,
                'video_list':video_list}
    return render_to_response('categorie.html', context, context_instance=RequestContext(request))




#@login_required(login_url="/login/")
def ProductFilterView(request, post_id, language):
    product = Product.objects.get(pk=post_id)
    filer_list = Image.objects.filter(folder_id = product.album)
    page_list = Page.objects.all()
    form = ProductForm()
    context = {'product': product,
    			'filer_list':filer_list,
                'page_list':page_list,
                'form':form}
    return render_to_response('detail.html', context, context_instance=RequestContext(request))



#@login_required(login_url="/login/")
def ProductFilterCategorydue(request, post_id):
    product_list = Product.objects.filter(category__in=post_id)
    category = Category.objects.get(pk=post_id)
    video_list = Video.objects.filter(active=True).filter(category_id=post_id).order_by('id')
    context = {'product_list': product_list,
                'category':category,
                'video_list':video_list}
    return render_to_response('categorie.html', context, context_instance=RequestContext(request))




#@login_required(login_url="/login/")
def ProductFilterViewdue(request, post_id):
    product = Product.objects.get(pk=post_id)
    filer_list = Image.objects.filter(folder_id = product.album)
    page_list = Page.objects.all()
    form = ProductForm()
    context = {'product': product,
                'filer_list':filer_list,
                'page_list':page_list,
                'form':form}
    return render_to_response('detail.html', context, context_instance=RequestContext(request))





###### customer #######
@login_required(login_url="/login/")
def customer_page(request):
    order_list = Order.objects.filter(user_id=request.user.id).order_by('-id')
    fatt = Fatturazione.objects.filter(user_id=request.user.id).first
    ind = IndirizzoSpedizione.objects.filter(user_id=request.user.id).first
    context = {
                'order_list':order_list,
                'fatt':fatt,
                'ind':ind
                }
    return render_to_response('customer.html', context, context_instance=RequestContext(request))



@login_required(login_url="/login/")
def add_customer_fatturazione(request):
    if request.method == "POST":
            form = AddFormFatturazione(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.user = request.user
                post.published_date = timezone.now()
                post.save()
                messages.success(request, 'Dati Fatturazione Inseriti')
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
                #return redirect('/', pk=post.pk)
            else:
                messages.error(request, 'Dati Fatturazione non inseriti')
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        messages.error(request, 'Dati Fatturazione non inseriti')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))



@login_required(login_url="/login/")
def update_customer_fatturazione(request, pk=None):
    obj = get_object_or_404(Fatturazione, pk=pk)
    form = AddFormFatturazione(request.POST or None, instance=obj)
    if request.method == 'POST':
        if form.is_valid():
           form.save()
           messages.success(request, 'Dati Fatturazione Aggiornati')
           return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    messages.error(request, 'Dati Fatturazione non aggiornati')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))



@login_required(login_url="/login/")
def add_customer_indirizzo_spedizione(request):
    if request.method == "POST":
            form = AddFormIndirizzoSpredizione(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.user = request.user
                post.published_date = timezone.now()
                post.save()
                messages.success(request, 'Dati Spedizione Inseriti')
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
                #return redirect('/', pk=post.pk)
            else:
                messages.error(request, 'Dati Spedizione non inseriti')
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        messages.error(request, 'Dati Spedizione non inseriti')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))



@login_required(login_url="/login/")
def update_customer_indirizzo_spedizione(request, pk=None):
    obj = get_object_or_404(IndirizzoSpedizione, pk=pk)
    form = AddFormIndirizzoSpredizione(request.POST or None, instance=obj)
    if request.method == 'POST':
        if form.is_valid():
           form.save()
           messages.success(request, 'Dati Indirizzo Spedizione Aggiornati')
           return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    messages.error(request, 'Dati Indirizzo Spedizione non aggiornati')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))



def logout_view(request):
    auth.logout(request)
    return HttpResponseRedirect('/')



def register_user_page(request):
    return render_to_response('registra.html', context_instance=RequestContext(request))



def add_user(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if User.objects.filter(username=request.POST.get('username')).exists():
            messages.error(request, 'Utente non creato... username gia presente')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            if form.is_valid():
                post = form.save(commit=False)
                pw = post.password
                post.set_password(pw)
                post.save()

                fatt_form = AddFormFatturazione(request.POST)
                fatt = fatt_form.save(commit=False)
                fatt.user_id = post.pk
                fatt.denominazione = request.POST.get('denominazione')
                fatt.piva = request.POST.get('piva')
                fatt.codfisc = request.POST.get('codfisc')
                fatt.indirizzo = request.POST.get('indirizzo')
                fatt.cap = request.POST.get('cap')
                fatt.citta = request.POST.get('citta')
                fatt.nazione = request.POST.get('nazione')
                fatt.telefono = request.POST.get('telefono')
                fatt.fax = request.POST.get('fax')
                fatt.e_mail = request.POST.get('email')
                fatt.published_date = timezone.now()
                fatt.save()

                sped_form = AddFormIndirizzoSpredizione(request.POST)
                sped = sped_form.save(commit=False)
                sped.user_id = post.pk
                sped.spedizione_published_date = timezone.now()
                sped.save()

                user = User.objects.get(pk=post.id) 
                ordi = "Registrazione:"
                psw = request.POST.get('password')
                subject, from_email, to = ordi, 'myshopfurniture@glocalnow.com', request.POST.get('email')
                text_content = 'This is an important message.'
                html_content = render_to_string('registrazione_email.html', {'user': user, 'psw': psw})
                msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
                msg.attach_alternative(html_content, "text/html")
                msg.send()

                subject, from_email, to = ordi, 'myshopfurniture@glocalnow.com', 'myshopfurniture@glocalnow.com'
                text_content = 'This is an important message.'
                html_content = render_to_string('registrazione_email.html', {'user': user, 'psw': psw})
                msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
                msg.attach_alternative(html_content, "text/html")
                msg.send()

                subject, from_email, to = ordi, 'myshopfurniture@glocalnow.com', 'pierangelo1982@gmail.com'
                text_content = 'This is an important message.'
                html_content = render_to_string('registrazione_email.html', {'user': user, 'psw': psw})
                msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
                msg.attach_alternative(html_content, "text/html")
                msg.send()

                messages.success(request, 'Utente Creato')
                return redirect('/login')
    else:
        messages.error(request, 'Utente non creato...')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))




## CART #############################
def add(request):
    cart = Cart(request.session)
    product = Product.objects.get(id=request.GET.get('product_id'))
    cart.add(product, price=product.price)
    messages.success(request, 'Prodotto Aggiunto al Carrello')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    #return HttpResponse("Added")


def show(request):
    if request.user.id:
        try:
            fatturazione = Fatturazione.objects.get(user_id=request.user.id)
            spedizione = IndirizzoSpedizione.objects.get(user_id=request.user.id)
            context = {'request':request, 'fatturazione': fatturazione, 'spedizione':spedizione}
            return render_to_response('cart.html', context, context_instance=RequestContext(request))
        except:
            return render(request, 'cart.html')
    else:
        return render(request, 'cart.html')


def remove(request, post_id):
    cart = Cart(request.session)
    product = Product.objects.get(pk=post_id)
    cart.remove(product)
    messages.error(request, 'Prodotto Eliminato dal Carrello')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))



## ORDER ########   ORDER    #########
@login_required(login_url="/login/")
def add_to_order(request):
    language = "it"
    session_language = "it"
    if 'lang' in request.session:
        session_language = request.session['lang']

    if request.method == "POST":
        form = AddOrderForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            cart = Cart(request.session)
            post.tot_price = 0
            if cart:
                post.tot_price = cart.total
            post.save()
            cart = Cart(request.session)
            for c in cart.items:
                form_item = AddOrderItemForm(request.POST)
                cart_item = form_item.save(commit=False)
                cart_item.order = post
                cart_item.product = c.product
                cart_item.quantity = c.quantity
                cart_item.price = c.product.price
                cart_item.save()
            
            ordine = Order.objects.get(pk=post.id) 
            fatturazione = Fatturazione.objects.get(user_id=request.user.id)
            consegna = IndirizzoSpedizione.objects.filter(user_id=request.user.id)
            ordi = "Ordine da: " + request.user.username
            subject, from_email, to = ordi, request.user.email, 'pierangelo1982@gmail.com'
            text_content = 'This is an important message.'
            if session_language == 'en':
                html_content = render_to_string('iban_emailuk.html', {'ordine': ordine, 'fatturazione':fatturazione, 'consegna':consegna})
            else:
                html_content = render_to_string('iban_email.html', {'ordine': ordine, 'fatturazione':fatturazione, 'consegna':consegna})
            msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()

            subject, from_email, to = ordi, request.user.email, 'myshopfurniture@glocalnow.com'
            text_content = 'This is an important message.'
            if session_language == 'en':
                html_content = render_to_string('iban_emailuk.html', {'ordine': ordine, 'fatturazione':fatturazione, 'consegna':consegna})
            else:
                html_content = render_to_string('iban_email.html', {'ordine': ordine, 'fatturazione':fatturazione, 'consegna':consegna})
            msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()

            subject, from_email, to = ordi, 'myshopfurniture@glocalnow.com', request.user.email
            text_content = 'This is an important message.'
            if session_language == 'en':
                html_content = render_to_string('iban_emailuk.html', {'ordine': ordine, 'fatturazione':fatturazione, 'consegna':consegna})
            else:
                html_content = render_to_string('iban_email.html', {'ordine': ordine, 'fatturazione':fatturazione, 'consegna':consegna})
            msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()

            cart = Cart(request.session)
            for c in cart.items:
                product_in_cart = Product.objects.get(pk=c.product.id)
                cart.remove(product_in_cart)

            messages.success(request, 'Ordine Effettuato')
            #return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            return redirect('/customer', pk=post.pk)
    else:
        messages.success(request, "Grazie di esserti loggato, ora puoi effettuare l'ordine")
        #return redirect('/show-cart/')
        return HttpResponseRedirect('/show-cart/')
        #form = AddOrderForm()
        #return render(request, 'order-form.html', {'form': form})


@login_required(login_url="/login/")
def order(request):
    order_list = Order.objects.filter(user_id=request.user.id).order_by('-id')
    context = {'order_list':order_list}
    return render_to_response('order.html', context, context_instance=RequestContext(request))


@login_required(login_url="/login/")
def orderDetail(request, post_id):
    order = Order.objects.get(pk=post_id)
    context = {'order':order}
    return render_to_response('orderdetail.html', context, context_instance=RequestContext(request))



######### PERSONALIZZAZIONE ##################
#@login_required(login_url="/login/")
def Personalizzazione(request, post_id, language):
    product = Product.objects.get(pk=post_id)
    filer_list = Image.objects.filter(folder_id = product.album)
    page_list = Page.objects.all()
    context = {'product': product,
                'page_list':page_list,
                'filer_list':filer_list}
    return render_to_response('personalizzazione.html', context, context_instance=RequestContext(request))


def add_personalizzazione(request):
    if request.method == "POST":
            form = AddPersonalizzaForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                #post.user = request.user
                post.published_date = timezone.now()
                post.save()
                user_email = request.POST.get('email_user')
                
                a=0
                for item in request.POST.getlist('moduli'):
                    form_item = PersonalizzaItemForm(request.POST)
                    post_item = form_item.save(commit=False)
                    post_item.personalizza = post
                    post_item.moduli_id = item
                    post_item.quantity = request.POST.getlist('quantity')[a]
                    post_item.published_date = timezone.now()
                    post_item.save()
                    a += 1

                personalizza = Personalizza.objects.get(pk=post.id) 
                ordine = "Richiesta preventivo da: " + user_email
                subject, from_email, to = ordine, user_email, 'pierangelo1982@gmail.com'
                text_content = 'This is an important message.'
                html_content = render_to_string('personalizza_email.html', {'personalizza': personalizza})
                msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
                msg.attach_alternative(html_content, "text/html")
                msg.send()

                subject, from_email, to = ordine, user_email, 'myshopfurniture@glocalnow.com'
                text_content = 'This is an important message.'
                html_content = render_to_string('personalizza_email.html', {'personalizza': personalizza})
                msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
                msg.attach_alternative(html_content, "text/html")
                msg.send()

                messages.success(request, 'Richiesta Inviata')
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
                #return redirect('/', pk=post.pk)
            else:
                messages.error(request, 'Richiesta non Inviata')
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        messages.error(request, 'Richiesta non Inviata')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))



############# Richiesta x sagitair ecc... ##################
def add_richiesta(request):
    if request.method == "POST":
            form = RichiestaForm(request.POST, request.FILES)
            if form.is_valid():
                #handle_uploaded_file(request.FILES['allegato'])
                post = form.save(commit=False)
                #post.user = request.user
                post.pub_date = timezone.now()
                post.allegato = request.FILES.get('allegato')
                #attach = request.FILES.get('allegato')
                post.save()
                user_email = request.POST.get('email')
                
                richiesta = Richiesta.objects.get(pk=post.id) 
                ordine = "Richiesta da: " + user_email
                subject, from_email, to = ordine, user_email, 'pierangelo1982@gmail.com'
                text_content = 'This is an important message.'
                html_content = render_to_string('richiesta_email.html', {'richiesta': richiesta})
                msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
                msg.attach_alternative(html_content, "text/html")
                #msg.attach(attach.name, attach.read(), attach.content_type)
                msg.send()

                subject, from_email, to = ordine, user_email, 'myshopfurniture@glocalnow.com'
                text_content = 'This is an important message.'
                html_content = render_to_string('richiesta_email.html', {'richiesta': richiesta})
                msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
                msg.attach_alternative(html_content, "text/html")
                #msg.attach(attach.name, attach.read(), attach.content_type)
                msg.send()

                messages.success(request, 'Richiesta Inviata')
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
                #return redirect('/', pk=post.pk)
            else:
                messages.error(request, 'Richiesta non Inviata')
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        messages.error(request, 'Richiesta non Inviata')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

############# search #############
def search(request):
    try:
        q = request.GET['q']
        product_list = Product.objects.filter(Q(name__icontains=q) | Q(code=q) | Q(descrizione__icontains=q))
        return render_to_response('price_list.html', {'product_list':product_list, 'q':q}, context_instance=RequestContext(request))
    except KeyError:
        messages.error(request, 'Nessuna Corrispondenza Trovata')
        #return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        return render_to_response('price_list.html', context_instance=RequestContext(request))



## PAGINE ########
def PageDetail(request, post_id, language):
    page = Page.objects.get(pk=post_id)
    context = {'page':page}
    return render_to_response('page.html', context, context_instance=RequestContext(request))

def PageDetaildue(request, post_id):
    page = Page.objects.get(pk=post_id)
    context = {'page':page}
    return render_to_response('page.html', context, context_instance=RequestContext(request))

## finiture
def finiture(request, language):
    colori_list = Color.objects.all()
    context = {'colori_list':colori_list}
    return render_to_response('finiture.html', context, context_instance=RequestContext(request))

def finituredue(request):
    colori_list = Color.objects.all()
    context = {'colori_list':colori_list}
    return render_to_response('finiture.html', context, context_instance=RequestContext(request))

## video
def video(request, language):
    video_list = Video.objects.all().order_by('?')
    context = {'video_list':video_list}
    return render_to_response('video.html', context, context_instance=RequestContext(request))

def videodue(request):
    video_list = Video.objects.all().order_by('?')
    context = {'video_list':video_list}
    return render_to_response('video.html', context, context_instance=RequestContext(request))

###### contatti ########
def contact(request):
    if request.method == 'POST': # If the form has been submitted...
        form = ContactForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            subject = 'MESSAGGIO DAL SITO myshop'
            #message = form.cleaned_data['messaggio']
            message = render_to_string('contact.txt', {'post': request.POST})
            sender = form.cleaned_data['email']
            cc_myself = False

            recipients = ['myshopfurniture@glocalnow.com']
            if cc_myself:
                recipients.append(sender)
        
            send_mail(subject, message, sender, recipients)
            messages.success(request, 'Messaggio inviato ti ricontatteremo al piu presto')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        messages.error(request, 'Messaggio non inviato')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

### contact home ######
def contactHome(request):
    if request.method == 'POST': # If the form has been submitted...
        form = ContactFormHome(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            subject = 'MESSAGGIO DAL SITO myshop'
            #message = form.cleaned_data['messaggio']
            message = render_to_string('contact_home.txt', {'post': request.POST})
            sender = form.cleaned_data['email']
            cc_myself = False

            recipients = ['myshopfurniture@glocalnow.com']
            if cc_myself:
                recipients.append(sender)
        
            send_mail(subject, message, sender, recipients)
            messages.success(request, 'Messaggio inviato ti ricontatteremo al piu presto')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        messages.error(request, 'Messaggio non inviato')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))



## newsletter
def add_newsletter(request):
    form = NewsletterForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
           form.save()
           messages.success(request, 'Indirizzo Aggiunto alla Newsletter')
           return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    messages.error(request, 'Indirizzo non registrato nella newsletter')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))




#######  GLOBALI #######
def CategoryMenuView(request):
    category_list = Category.objects.all()
    context = {'category_list': category_list}
    return context

### setting language session
def language(request, language='it'):
    response = HttpResponse("setting language to %s" % language)
    response.set_cookie('lang', language)
    request.session['lang'] = language
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def stagioni(request):
    return season


    
