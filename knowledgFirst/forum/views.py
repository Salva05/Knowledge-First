from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import *

def index(request):
    template = loader.get_template('index.html')
    context = {}
    return HttpResponse(template.render(context, request))

def elenco(request):
    template = loader.get_template('elenco.html')
    posts = Post.objects.all()

    context = {
        'posts': posts
    }
    return HttpResponse(template.render(context, request))

def dettaglio(request, id):
    template = loader.get_template('dettaglio.html')

    target_post = Post.objects.get(pk=id)

    comments = Comment.objects.all().filter(post=target_post)

    context = {
        'post': target_post,
        'comments': comments
    }
    return HttpResponse(template.render(context, request))