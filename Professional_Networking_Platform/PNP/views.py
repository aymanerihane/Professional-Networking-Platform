# Create your views here.
from django.shortcuts import render , get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User as auth_user
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import User, Post, Room, Like,Comment, Student, Teacher,Entreprise, Cv
from .forms import SignUpForm, NewPost, CVForm
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

#page of choice entreprise account or school account
def signUp1(request):
    if request.user.is_authenticated:
        return redirect('PNP:firstPage')
    return render(request, 'registration/signUp.html', {})

# commun singup 1
def signUp(request,choix):

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)  # user is a User object now
            
            #prendre la partie apres la @ de l'email
            if choix == 1:
                afterAt = user.email.split('@')[1]
                if afterAt == 'etu.uae.ac.ma':
                    request.session['role'] = 1
                elif afterAt == 'uae.ac.ma':
                    request.session['role'] = 2
                else:
                    form = UserCreationForm()
                    return render(request, 'registration/signUp1.html', {"form": form, 'error': 'Email non valide'})
            elif choix == 2:
                request.session['role'] = 3
            user.save()
            request.session['user_id'] = user.id
            # make auto  auth
            return redirect('PNP:signUp2')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signUp1.html', {"form": form})

# commun singup 2
def signUp2(request):
    if request.method == "POST":
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            pnp_user = form.save(commit=False)
            role = request.session.get('role')
            userid = request.session.get('user_id')
            if userid is not None:
                pnp_user.user_id = userid
                pnp_user.role = role
                pnp_user.save()
                if role ==1:
                    cne = request.POST.get('CNE')
                    if cne is not None:  # Make sure cne is not None
                        user = User.objects.get(user_id=userid)  # Get the User instance with id=userid
                        Student.create_student(user, cne)  # Call create_student on the Student class
                        return redirect('PNP:signUpStud')
                    else :
                        return HttpResponse("CNE is missing")
                elif role == 2:
                    matricule = request.POST.get('matricule')
                    if matricule is not None:  # Make sure cne is not None
                        user = User.objects.get(id=userid)  # Get the User instance with id=userid
                        Teacher.create_teacher(user, matricule)  # Call create_student on the Student class
                        return redirect('PNP:signUpTeach')
                    else :
                        return HttpResponse("Matricule is missing")
                else:
                    ice = request.POST.get('ice')
                    if ice is not None:  # Make sure cne is not None
                        user = User.objects.get(id=userid)  # Get the User instance with id=userid
                        # Entreprise.create_entreprise(user, ice)  # Call create_student on the Student class
                        return redirect('PNP:signUpEntre')
            else:
                # Handle missing user id here
                return HttpResponse("User id is missing")
    else:
        form = SignUpForm()
    return render(request, 'registration/signUp2.html', {"form": form,"role": 1 if request.session.get('role') == 1 else 2})

# student singup (page3)
def signUpStud(request):
    if request.method == "POST":
        cv_form = CVForm(request.POST)
        print("###############")
        if cv_form.is_valid():
            cv = cv_form.save(commit=False)
            userid = request.session.get('user_id')
            cv.user_id = userid
            company = cv_form.cleaned_data['company']
            job_title = cv_form.cleaned_data['job_title']
            start_date = cv_form.cleaned_data['start_date']
            end_date = cv_form.cleaned_data['end_date']
            description = cv_form.cleaned_data['description']
            school = cv_form.cleaned_data['school']
            degree = cv_form.cleaned_data['degree']
            start_dateE = cv_form.cleaned_data['start_dateE']
            end_dateE = cv_form.cleaned_data['end_dateE']
            if company is not None and job_title is not None and start_date is not None and end_date is not None and description is not None:
                cv.experiences = Cv.tojson_experience(company, job_title, start_date, end_date, description)
            else:
                return HttpResponse("Experience is missing")
            if school is not None and degree is not None and start_dateE is not None and end_dateE is not None:
                cv.educations = Cv.tojson_education(school, degree, start_dateE, end_dateE)
            else:
                return HttpResponse("Education is missing")
            cv.skills = Cv.skills_tojson(cv_form.cleaned_data['skills'])
            cv.languages = Cv.languages_tojson(cv_form.cleaned_data['languages'])
            cv.save()  # Enregistrer le CV
            return redirect('PNP:login')  # Rediriger vers la page de connexion après inscription
    else:
        cv_form = CVForm()
    return render(request, 'registration/signUpStud.html', {"form": cv_form})

# entreprise singup (page3)
def signUpEntre(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
    else:
        form = UserCreationForm()
    return render(request, 'registration/signUp1.html', {"form": form})


@login_required
def profile(request,username):
    user = auth_user.objects.get(username=username)
    pnp_user = User.objects.get(user_id=user.id)
    if request.user.username != username:
        pnp_user.number_of_profile_visits = pnp_user.number_of_profile_visits + 1
    pnp_user.save()
    context = {
        'user': auth_user.objects.get(username=username),
        'isMe': True if request.user.username == username else False,
        'isFriend': True if User.objects.get(user_id=request.user.id).friends.filter(user_id=user.id).exists() else False
    }
    return render(request,'profilePage/profile.html' , context)

# metting pages

##metting choix page
def mettingPage(request):
    userRole = User.objects.get(user_id=request.user.id).role
    if userRole == 1:
        return redirect('PNP:joinMetting')
    return render(request,'messagePage/mettingPage.html' , {})

##metting create page
def metting(request):
    context = {
        'username': request.user.username
    }
    return render(request,'messagePage/createMetting.html' , context)

##metting join page
def joinMetting(request):
    userRole = User.objects.get(user_id=request.user.id).role
    if request.method == 'POST':
        room_id = request.POST['roomID']
        # if room_id in User.objects.get(id=request.user.id).rooms.all():
        return redirect('/metting/?roomID='+room_id)
    context = {
        'role': userRole
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
    #check if the current user is likerd the post or not
    for post in posts:
        if Like.objects.filter(post_id=post.id, user_id=current_user.id).exists():
            post.liked = True
        else:
            post.liked = False
    posts_with_time_since = [{
        'post': post,
        'time_since': time_since(post.created_at)
    } for post in posts]
    context = {
        'posts': posts_with_time_since,
        'user': user,
        'number_of_visits': current_user.number_of_profile_visits,
        'number_of_posts': Post.objects.filter(user_id=current_user.id).count(),
        'number_of_friends': current_user.friends.count(),
        'friends': friends,
    }
    return render(request,'firstPage/fisrtPage.html' , context)


# add friend
def addFriend(request, username):
    user = auth_user.objects.get(username=username)  # get User instance from User model
    friend= User.objects.get(user_id=user.id)
    current_user = User.objects.get(user_id=request.user.id)
    if not current_user.friends.filter(user_id=user.id).exists():
        current_user.friends.add(friend)
    else:
        current_user.friends.remove(friend)
    return redirect('PNP:profile', username=username)

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



