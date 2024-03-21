from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import *

def index(request):
    template = loader.get_template('index.html')

    latest_posts = Post.objects.all().order_by('-pub_date')[:5]
    context = {
        'latest_posts': latest_posts
    }
    return HttpResponse(template.render(context=context, request=request))

def elenco(request):
    template = loader.get_template('elenco.html')
    posts = Post.objects.all()

    context = {
        'posts': posts
    }
    return HttpResponse(template.render(context, request))

def detail(request, id):
    template = loader.get_template('detail.html')

    target_post = Post.objects.get(pk=id)

    replies = Reply.objects.all().filter(post=target_post)

    context = {
        'post': target_post,
        'replies': replies
    }
    return HttpResponse(template.render(context, request))