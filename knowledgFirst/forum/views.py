from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError
from django.contrib.auth import login, logout

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

    user_authenticated = request.user.is_authenticated
    
    context = {
        'latest_posts': latest_posts,
        'most_quoted': most_quoted,
        'most_active': most_active,
        'members': members,
        'categories': categories,
        'user_authenticated': user_authenticated
    }
    
    return HttpResponse(template.render(context=context, request=request))

def elenco(request):
    template = loader.get_template('elenco.html')
    posts = Post.objects.all()
    categories = Post.get_categories()
    user_authenticated = request.user.is_authenticated

    context = {
        'posts': posts,
        'categories': categories,
        'user_authenticated': user_authenticated
    }
    return HttpResponse(template.render(context, request))

def specific_list(request, type):
    template = loader.get_template('specific_list.html')
    topics = Post.objects.all().filter(category=type)
    categories = Post.get_categories()
    user_authenticated = request.user.is_authenticated

    context = {
        'topics': topics,
        'categories': categories,
        'user_authenticated': user_authenticated
    }
    return HttpResponse(template.render(context, request))

def search(request):
    template = loader.get_template('search.html')
    query = request.GET.get('q')
    topics = Post.objects.filter(title__icontains=query) | Post.objects.filter(content__icontains=query)
    categories = Post.get_categories()
    user_authenticated = request.user.is_authenticated

    context = {
        'topics': topics,
        'query': query,
        'categories': categories,
        'user_authenticated': user_authenticated
    }
    return HttpResponse(template.render(context, request))

def detail(request, id):
    template = loader.get_template('detail.html')

    target_post = Post.objects.get(pk=id)

    replies = Reply.objects.all().filter(post=target_post)
    categories = Post.get_categories()
    user_authenticated = request.user.is_authenticated

    context = {
        'post': target_post,
        'replies': replies,
        'categories': categories,
        'user_authenticated': user_authenticated
    }
    return HttpResponse(template.render(context, request))

def signup(request):
    user_authenticated = request.user.is_authenticated

    categories = Post.get_categories()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        email = request.POST.get('email')
        if not email:
            return render(request, 'signup.html', {'form': form, 'email_error': 'Email is required', 'categories': categories, 'user_authenticated': user_authenticated})
        
        try:
            EmailValidator()(email)
        except ValidationError:
            return render(request, 'signup.html', {'form': form, 'email_error': 'Invalid email format', 'categories': categories, 'user_authenticated': user_authenticated})

        if Profile.objects.filter(email=email).exists():
            return render(request, 'signup.html', {'form': form, 'email_error': 'Email already in use', 'categories': categories, 'user_authenticated': user_authenticated})
        
        if form.is_valid():
            # Save the standard django user
            user = form.save()

            # Create the profile for the user
            avatar = request.FILES.get('avatar', None)
            print(avatar)
            if avatar == None:
                avatar = 'static/avatars/user.png'
                
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
    return render(request, 'signup.html', {'form': form, 'categories': categories, 'user_authenticated': user_authenticated})

def signup_success(request):
    categories = Post.get_categories()
    user_authenticated = request.user.is_authenticated

    return render(request, 'signup_success.html', {'categories': categories, 'user_authenticated': user_authenticated})

def signin(request):
    categories = Post.get_categories()
    user_authenticated = request.user.is_authenticated

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not username or not password:
            return render(request, 'signin.html', {'error': 'Username and password are required', 'categories': categories, 'user_authenticated': user_authenticated})

        if not User.objects.filter(username=username).exists():
            return render(request, 'signin.html', {'error': 'Username not found', 'categories': categories, 'user_authenticated': user_authenticated})
        
        user = User.objects.get(username=username)

        if not user.check_password(password):
            return render(request, 'signin.html', {'error': 'Incorrect password', 'categories': categories, 'user_authenticated': user_authenticated})
        
        login(request, user)

        return redirect('index')
    return render(request, 'signin.html', {'categories': categories, 'user_authenticated': user_authenticated})

def signout(request):
    logout(request)
    return redirect('index')

def profile(request):
    template = loader.get_template('profile.html')
    categories = Post.get_categories()

    is_admin = False
    user = request.user

    if user.is_superuser:  # Check if the user is a superuser (admin)
        is_admin = True
    else:
        try:
            user_profile = Profile.objects.get(user=user)
        except Profile.DoesNotExist:
            is_admin = True

    if is_admin:
        context = {
            'categories': categories,
            'is_admin': is_admin,
            'message': 'You are an admin'
        }
    else:
        context = {
            'categories': categories,
            'user_profile': user_profile,
        }

    return HttpResponse(template.render(context, request))
