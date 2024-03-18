# Create your views here.
from django.shortcuts import render , get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User as auth_user
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import User, Post, Room, Like,Comment
from .forms import SignUpForm, NewPost
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login as auth_login
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
from django.utils import timezone


# import datetime
# @login_required

# sign up and login
def loginRed(request):
    return redirect('PNP:login')
@csrf_exempt
def logincheck(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            return JsonResponse({'correct': True})
        else:
            return JsonResponse({'correct': False})

def signUp(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # user is a User object now
            request.session['user_id'] = user.id  # Store user id in session
            #prendre la partie apres la @ de l'email
            afterAt = user.email.split('@')[1]
            if(afterAt == 'etu.uae.ac.ma'):
                request.session['role'] = 1
            else:
                request.session['role'] = 2
            return redirect('PNP:signUp2')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signUp.html', {"form": form})

def signUp2(request):
    if request.method == "POST":
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            user_id = request.session.get('user_id')  # Retrieve user id from session
            role = request.session.get('role')
            if user_id is not None:
                form.user_id = user_id
                form.role = role
                form.save()
                return redirect('PNP:login')
            else:
                # Handle missing user id here
                return HttpResponse("User id is missing")
    else:
        form = SignUpForm()
    return render(request, 'registration/signUp2.html', {"form": form})


@login_required
def profile(request,username):
    context = {
        'user': auth_user.objects.get(username=username)
    }
    return render(request,'profilePage/profile.html' , context)

# metting pages

##metting choix page
def mettingPage(request):
    context = {
    }
    return render(request,'messagePage/mettingPage.html' , context)

##metting create page
def metting(request):
    context = {
        'username': request.user.username
    }
    return render(request,'messagePage/createMetting.html' , context)

##metting join page
def joinMetting(request):
    if request.method == 'POST':
        room_id = request.POST['roomID']
        # if room_id in User.objects.get(id=request.user.id).rooms.all():
        return redirect('/metting/?roomID='+room_id)
    context = {
    }
    return render(request,'messagePage/joinMetting.html' , context)

# messaging page
def messaging(request):
    userID = request.user.id
    userInfo = User.objects.get(user_id=userID)
    rooms = userInfo.rooms.all()
    context = {
        'rooms': rooms
    }
    return render(request,'messagePage/messagePage.html' , context)

def room(request, room_id):
    room = get_object_or_404(Room, pk=room_id)
    print(room)
    return render(request, 'messagePage/room.html', {'room': room})

# first page after login
def firstPage(request):
    friends = User.objects.get(user_id=request.user.id).friends.all()
    current_user = User.objects.get(user_id=request.user.id)
    user = request.user
    posts = Post.objects.filter(Q(user_id__in=friends) | Q(user_id=current_user.id)).order_by('-created_at')
    posts_with_time_since = [{
        'post': post,
        'time_since': time_since(post.created_at)
    } for post in posts]
    context = {
        'posts': posts_with_time_since,
        'user': user,
    }
    return render(request,'firstPage/fisrtPage.html' , context)


# add friend
def addFriend(request, username):
    user = auth_user.objects.get(username=username)  # get User instance from User model
    friend= User.objects.get(user_id=user.id)
    current_user = User.objects.get(user_id=request.user.id)
    current_user.friends.add(friend)
    return redirect('PNP:firstPage')

# create post
def createPost(request):
    if request.method == 'POST':
        form = NewPost(request.POST)
        if form.is_valid():
            content = form.cleaned_data['content']
            link = form.cleaned_data['link']
            media = form.cleaned_data['media']
            user_id = request.user.id
            Post.create_post(content, user_id, link, media)
            return redirect('PNP:firstPage')
    else:
        form = NewPost()
    return render(request, 'firstPage/createPost.html', {'form': form})


#network page
def network(request):
    context = {
        'friends' : User.objects.get(user_id=request.user.id).friends.all()
    }
    return render(request,'networkPage/networkPage.html' , context)

#classroom page
def classroom(request):
    context = {
    }
    return render(request,'classroom/rooms.html' , context)


#post like
def like(request, postid):
    post = Post.objects.get(id=postid)
    user = User.objects.get(user_id=request.user.id)
    if Like.objects.filter(post_id=postid, user_id=user.id).exists():
        post.num_likes = post.num_likes - 1
        Like.delete_like(user, post)
        print('unlike')
    else:
        Like.create_like(user, post)
        post.num_likes = post.num_likes + 1
        print('like')
    
    post.save()
    return JsonResponse({'success': True,'likes': post.num_likes})

#post comments
def comment(request, postid):
    post = Post.objects.get(id=postid)
    user = User.objects.get(user_id=request.user.id)
    comment=request.POST.get('comment')
    Comment.create_comment(user, post,comment)
    post.num_comments = post.num_comments + 1
    print('comment send')
    post.save()
    return JsonResponse({'success': True,'likes': post.num_comments})












# time since function

def time_since(d):
    now = timezone.now()
    print(now)
    diff = now - d

    seconds_in_day = 24 * 60 * 60
    seconds_in_hour = 60 * 60
    seconds_in_minute = 60

    if diff.days > 365:
        return f'{diff.days // 365} years'
    elif diff.days > 30:
        return f'{diff.days // 30} months'
    elif diff.days > 0:
        return f'{diff.days} days'
    elif diff.seconds > seconds_in_hour:
        return f'{diff.seconds // seconds_in_hour} hours'
    elif diff.seconds > seconds_in_minute:
        return f'{diff.seconds // seconds_in_minute} minutes'
    else:
        return 'just now'

