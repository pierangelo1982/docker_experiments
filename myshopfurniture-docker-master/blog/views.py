# coding=utf-8
from django.shortcuts import render
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.views.generic import ListView, DetailView
from django.template.loader import render_to_string
from blog.models import *
from filer.models import *
# Create your views here.


def blogView(request, language):
	blog_list = Blog.objects.all().order_by('-pub_date')
	context = {'blog_list':blog_list}
	return render_to_response('blog.html', context, context_instance=RequestContext(request))

def blogDetail(request, post_id, language):
	blog = Blog.objects.get(pk=post_id)
	context = {'blog':blog}
	return render_to_response('blog-detail.html', context, context_instance=RequestContext(request))

def blogViewdue(request):
	blog_list = Blog.objects.all().order_by('-pub_date')
	context = {'blog_list':blog_list}
	return render_to_response('blog.html', context, context_instance=RequestContext(request))

def blogDetaildue(request, post_id):
	blog = Blog.objects.get(pk=post_id)
	context = {'blog':blog}
	return render_to_response('blog-detail.html', context, context_instance=RequestContext(request))