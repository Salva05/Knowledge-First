from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import *

def index(request):
    template = loader.get_template('index.html')

    latest_posts = Post.objects.all().order_by('-pub_date')[:5]
    most_quoted = Post.objects.all().order_by('-likes')[:5]
    most_active = Profile.objects.all().order_by('-replies')[:5]
    members = Profile.objects.all()
    categories = Post.get_categories()
    
    context = {
        'latest_posts': latest_posts,
        'most_quoted': most_quoted,
        'most_active': most_active,
        'members': members,
        'categories': categories
    }
    
    return HttpResponse(template.render(context=context, request=request))

def elenco(request):
    template = loader.get_template('elenco.html')
    posts = Post.objects.all()
    
    context = {
        'posts': posts
    }
    return HttpResponse(template.render(context, request))

def specific_list(request, type):
    template = loader.get_template('specific_list.html')
    topics = Post.objects.all().filter(category=type)
    
    context = {
        'topics': topics,
    }
    return HttpResponse(template.render(context, request))

def search(request):
    template = loader.get_template('search.html')
    query = request.GET.get('q')
    topics = Post.objects.filter(title__icontains=query) | Post.objects.filter(content__icontains=query)
    
    context = {
        'topics': topics,
        'query': query
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