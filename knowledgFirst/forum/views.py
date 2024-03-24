from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError
from .models import *

def index(request):
    template = loader.get_template('index.html')

    latest_posts = Post.objects.all().order_by('-pub_date')[:5]

    most_quoted = Post.objects.all().order_by('-likes')
    most_quoted = [post for post in most_quoted if post.likes > 0][:5]

    most_active = Profile.objects.all().order_by('-replies')
    most_active = [post for post in most_active if post.replies > 0][:5]

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

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        email = request.POST.get('email')
        if not email:
            return render(request, 'signup.html', {'form': form, 'email_error': 'Email is required'})
        
        try:
            EmailValidator()(email)
        except ValidationError:
            return render(request, 'signup.html', {'form': form, 'email_error': 'Invalid email format'})

        if Profile.objects.filter(email=email).exists():
            return render(request, 'signup.html', {'form': form, 'email_error': 'Email already in use'})
        
        if form.is_valid():
            # Save the standard django user
            user = form.save()

            # Create the profile for the user
            avatar = request.FILES.get('avatar', None)
            interests = request.POST.get('interests', None)
            email = request.POST.get('email')

            # Create a new profile instance linked to the user
            profile = Profile.objects.create(
                user=user,
                avatar=avatar,
                interests=interests,
                email=email
            ) 

            return redirect('signup_success')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def signup_success(request):
    return render(request, 'signup_success.html')