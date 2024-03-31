from django.shortcuts import render, redirect, get_object_or_404
from django.template import loader
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError
from django.db.models import F, Count
from django.contrib.auth import login, logout



from .models import *

def index(request):
    template = loader.get_template('index.html')

    latest_posts = Post.objects.all().order_by('-pub_date')[:5]

    most_quoted = Post.objects.annotate(num_likes=Count('likes')).filter(num_likes__gt=0).order_by('-num_likes')[:5]

    most_active = Profile.objects.annotate(num_replies=Count('reply')).filter(num_replies__gt=0).order_by('-num_replies')[:5]

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

    profile = None
    liked_by_user = None
    replies_liked_by_user = {}
    
    user_authenticated = request.user.is_authenticated
    if user_authenticated and not request.user.is_superuser:
        # Create a dictionary to store whether the user liked each reply
        for reply in replies:
            if reply.reply_like.filter(user=request.user.profile).exists():
                replies_liked_by_user[reply.id] = True
            else:
                replies_liked_by_user[reply.id] = False

        user = request.user
        profile = Profile.objects.get(user=user)
        p = Post.objects.get(pk=id)
        liked_by_user = p.likes.filter(user=request.user.profile).exists()

    
    context = {
        'post': target_post,
        'replies': replies,
        'categories': categories,
        'user_authenticated': user_authenticated,
        'profile': profile,
        'liked_by_user': liked_by_user,
        'replies_liked_by_user': replies_liked_by_user
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

            #sign in the user
            login(request, user)

            return redirect('signup_success')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form, 'categories': categories, 'user_authenticated': user_authenticated})

def signup_success(request):
    categories = Post.get_categories()
    user_authenticated = request.user.is_authenticated
    user = request.user
    return render(request, 'signup_success.html', {'categories': categories, 'user_authenticated': user_authenticated, 'user': user})

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
    user_authenticated = request.user.is_authenticated
    
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
            'message': 'You are an admin',
            'user_authenticated': user_authenticated,
        }
    else:
        context = {
            'categories': categories,
            'user_profile': user_profile,
            'user_authenticated': user_authenticated,
        }

    return HttpResponse(template.render(context, request))

def new_topic(request):
    user_authenticated = request.user.is_authenticated

    if not request.user.is_authenticated:
        return redirect('required_signin')
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        category = request.POST.get('category')
        author = request.user.profile
        post = Post.objects.create(title=title, content=content, category=category, author=author)

        # increace total topics of the user by one
        author.total_posts = F('total_posts') + 1
        author.save()
        
        return redirect('detail', id=post.id)
    return render(request, 'new_topic.html', {'categories': Post.get_categories(), 'user_authenticated': user_authenticated})

def required_signin(request):
    user_authenticated = request.user.is_authenticated

    return render(request, 'required_signin.html', {'categories': Post.get_categories(), 'user_authenticated': user_authenticated})

def submit_reply(request):
    if request.method == 'POST':
        reply_entity = request.POST.get('entity_type')
        if reply_entity == 'reply':
            text = request.POST['reply']
            post_id = request.POST['post_id']
            reply_id = request.POST['entity_id']
            
            rpl = Reply.objects.create(
                content=text,
                author=request.user.profile,
                reply_to_reply=Reply.objects.get(pk=reply_id),
                post=Post.objects.get(pk=post_id)
            )
            print(Reply.objects.get(pk=reply_id).content)
        else:
            text = request.POST['reply']
            post_id = request.POST['post_id']
            rpl = Reply.objects.create(
                content=text,
                author=request.user.profile,
                post=Post.objects.get(pk=post_id)
            )
        # increase user's replies
        author=request.user.profile
        author.replies = F('replies') + 1
        author.save()
        
        return redirect('detail', id=post_id)
    return HttpResponse("Invalid request or data", status=400)

def delete_topic(request, id):
    post = get_object_or_404(Post, pk=id)
    post.delete()
    return redirect('elenco')

def delete_reply(request):
    if request.method == 'POST':
        reply_id = request.POST['reply_id']
        post_id = request.POST['post_id']
        reply = Reply.objects.get(pk=reply_id)
        reply.content = '[deleted]'
        reply.save()
    return redirect('detail', id=post_id)

def post_like(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    if PostLike.objects.filter(post=post, user=request.user.profile).exists():
        return JsonResponse({'success': False, 'message': 'User already liked this post.'})
    else:
        post_like = PostLike(post=post, user=request.user.profile)
        post_like.save()

        post.total_likes += 1
        post.save()
        return JsonResponse({'success': True, 'message': 'Post liked successfully.'})
    
def reply_like(request, reply_id):
    reply = get_object_or_404(Reply, pk=reply_id)
    print('view chiamata')

    if ReplyLike.objects.filter(reply=reply, user=request.user.profile).exists():
        return JsonResponse({'success': False, 'message': 'User already liked this post.'})
    else:
        reply_like = ReplyLike(reply=reply, user=request.user.profile)
        reply_like.save()

        reply.likes += 1
        reply.save()
        return JsonResponse({'success': True, 'message': 'Post liked successfully.'})