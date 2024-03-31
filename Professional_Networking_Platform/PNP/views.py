# Create your views here.
import random
from django.shortcuts import render , get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User as auth_user
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import User, Post, Room, Like,Comment, Student, Teacher,Entreprise, Cv, Cours,PostMedia,FriendRequest,Message,MessageMedia,Devoir,Documentation
from .forms import SignUpForm, CVForm,ExperienceForm,EducationForm,SkillsForm,LanguagesForm,AboutForm,EditCV,EditProfile, CoursForm,RoomForm,DuscForm,DevoirForm, DocumentationForm,AddMember
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login as auth_login
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q,Count
from django.utils import timezone
from django.contrib.contenttypes.models import ContentType
import json ,os
from django.conf import settings
import os
from django.http import JsonResponse
from django.core.files import File


# import datetime
# @login_required

# sign up and login
def loginRed(request):
    return redirect('PNP:login')
@csrf_exempt
def logincheck(request):
    if request.user.is_authenticated:
        redirect('PNP:firstPage')
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
        redirect('PNP:firstPage')
    if request.user.is_authenticated:
        return redirect('PNP:firstPage')
    return render(request, 'registration/signUp.html', {})

# commun singup 1
def signUp(request,choix):
    if request.user.is_authenticated:
        redirect('PNP:firstPage')
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
    if request.user.is_authenticated:
        redirect('PNP:firstPage')
    if request.method == "POST":
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            pnp_user = form.save(commit=False)
            role = request.session.get('role')
            userid = request.session.get('user_id')
            print(role)
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
                        Entreprise.create_entreprise(user, ice)  # Call create_student on the Student class
                        return redirect('PNP:signUpEntre')
            else:
                # Handle missing user id here
                return HttpResponse("User id is missing")
    else:
        form = SignUpForm()
    return render(request, 'registration/signUp2.html', {"form": form,"role": request.session.get('role')})

# student singup (page3)
def signUpStud(request):
    if request.user.is_authenticated:
        redirect('PNP:firstPage')
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
                cv.add_experience(company=company, job_title=job_title,  start_date=start_date, end_date=end_date, description=description)
            else:
                return HttpResponse("Experience is missing")
            if school is not None and degree is not None and start_dateE is not None and end_dateE is not None:
                cv.add_education(school, degree, start_dateE, end_dateE)
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
    if request.user.is_authenticated:
        redirect('PNP:firstPage')
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
    else:
        form = UserCreationForm()
    return render(request, 'registration/signUp1.html', {"form": form})

# profile views
def profile(request, username):
    the_user = auth_user.objects.get(username=username)
    cv = Cv.objects.get(user_id=the_user.id)
    cv.skills = json.loads(cv.skills)
    cv.languages = json.loads(cv.languages)
    pnp_user = User.objects.get(user_id=the_user.id)
    posts = Post.objects.filter(user_id=pnp_user.id).all().order_by('-created_at')
    context = {}


    for post in posts:
        post.liked = Like.objects.filter(post_id=post.id, user_id=pnp_user.id).exists()
    posts_with_time_since = [{
        'post': post,
        'time_since': time_since(post.created_at),
        'numberComments': Comment.objects.filter(object_id=post.id).count()
    } for post in posts]
    

    if request.user.is_authenticated:
        current_user = User.objects.get(user_id=request.user.id)
        #take all request of the current user

        all_requests = FriendRequest.objects.filter(receiver=current_user.id)
        segg = seggestedFriends(request)
        
        if current_user != pnp_user:
            pnp_user.number_of_profile_visits += 1
            pnp_user.save()
        
        room = Room.objects.filter(participent__user__username=username).annotate(participent_count=Count('participent')).filter(participent_count__lt=2).first()

        if room is not None:
            room_id = room.room_ID
        else:
            room_id = None  # or set a default value, or handle this situation differently

        #get post medias

        context.update({
            'auth_user': request.user,
            'user': current_user,
            'request_recived': all_requests,
            'requestsend': FriendRequest.objects.filter(sender=the_user.id).exists(),
            'isMe': request.user.username == username,
            'isFriend': current_user.friends.filter(user_id=the_user.id).exists(),
            'segguestedFriends': segg,
            'id': room_id,
        })

    context.update({
        'the_user': the_user,
        'cv': cv,
        'is_private': pnp_user.Visibility == 'private',
        'posts': posts_with_time_since,
    })


    return render(request, 'profilePage/profile.html', context)
def formProfile(request, id, username):
    print("entred")
    form_classes = {
        0: AboutForm,
        1: ExperienceForm,
        2: EducationForm,
        3: SkillsForm,
        4: LanguagesForm,
        5: EditCV,
        6: EditProfile,
    }

    if id not in form_classes:
        return HttpResponse("Error")

    FormClass = form_classes[id]

    if request.method == "POST":
        form = FormClass(request.POST, request.FILES)
        if form.is_valid():
            user = auth_user.objects.get(username=username)
            pnp_user = User.objects.get(user_id=user.id)
            cv = Cv.objects.get(user_id=user.id)
            if id == 0:
                cv.about = form.cleaned_data['about']
                cv.save()
                return redirect('PNP:profile', username=request.user.username)
            elif id == 1:
                cv.add_experience(
                    company=form.cleaned_data['company'],
                    job_title=form.cleaned_data['job_title'],
                    start_date=form.cleaned_data['start_date'],
                    end_date=form.cleaned_data['end_date'],
                    description=form.cleaned_data['description']
                )
                return redirect('PNP:profile', username=request.user.username)
            elif id == 2:
                cv.add_education(
                    school=form.cleaned_data['school'],
                    degree=form.cleaned_data['degree'],
                    start_dateE=form.cleaned_data['start_dateE'],
                    end_dateE=form.cleaned_data['end_dateE']
                )
                return redirect('PNP:profile', username=request.user.username)
            elif id == 3:
                cv.add_skills(form.cleaned_data['skills'])
                cv.save()
                return redirect('PNP:profile', username=request.user.username)
            elif id == 4:
                cv.add_languages(form.cleaned_data['languages'])
                cv.save()
                return redirect('PNP:profile', username=request.user.username)
            elif id == 5:
                #delete the previews file local from media cv
                pnp_user.deleteFile()
                pnp_user.cv = form.cleaned_data['cv']
                pnp_user.save()
                return redirect('PNP:profile', username=request.user.username)
            elif id == 6:
                user.username = form.cleaned_data['username']
                user.email = form.cleaned_data['email']
                #check if the old password is correct
                if form.cleaned_data['old_password'] != '':
                    if user.check_password(form.cleaned_data['old_password']):
                        user.set_password(form.cleaned_data['new_password'])
                    else:
                        request.session['error'] = 'Old password is incorrect'
                        return redirect('PNP:profile', username=request.user.username)
                pnp_user.phone = form.cleaned_data['phone']
                pnp_user.address = form.cleaned_data['address']
                pnp_user.city = form.cleaned_data['city']
                pnp_user.country = form.cleaned_data['country']
                pnp_user.Visibility = form.cleaned_data['Visibility']
                pnp_user.save()
                user.save()
                return redirect('PNP:profile', username=request.user.username)
        else:
            if request.session.get('error') is not None:
                error = request.session.get('error')
                del request.session['error']
            return render(request, 'profilePage/formProfile.html', {"form": form, "id": id, "username": username,"error": error})
    else:  # GET request
        form = FormClass()
        if id == 6:
            form.fields['username'].initial = username
            form.fields['email'].initial = User.objects.get(user_id=request.user.id).user.email
            form.fields['phone'].initial = User.objects.get(user_id=request.user.id).phone
            form.fields['address'].initial = User.objects.get(user_id=request.user.id).address
            form.fields['city'].initial = User.objects.get(user_id=request.user.id).city
            form.fields['country'].initial = User.objects.get(user_id=request.user.id).country
            form.fields['Visibility'].initial = User.objects.get(user_id=request.user.id).Visibility


    return render(request, 'profilePage/formProfile.html', {"form": form, "id": id, "auth_user": request.user})

def formEducation(request, id, username):
    if request.method == "POST":
        form = EducationForm(request.POST)
        if form.is_valid():
            user = auth_user.objects.get(username=username)
            cv = Cv.objects.get(user_id=user.id)
            cv.update_etud(
                id=id,
                school=form.cleaned_data['school'],
                degree=form.cleaned_data['degree'],
                start_dateE=form.cleaned_data['start_dateE'],
                end_dateE=form.cleaned_data['end_dateE']
            )
            return redirect('PNP:profile', username=request.user.username)
    else:
        cv = Cv.objects.get(user_id=request.user.id)
        education = next((edu for edu in cv.educations if edu['id'] == id), None)

        if education is not None:
            form = EducationForm()
            form.fields['school'].initial = education['school']
            form.fields['degree'].initial = education['degree']
            form.fields['start_dateE'].initial = education['start_date']
            form.fields['end_dateE'].initial = education['end_date']

    return render(request, 'profilePage/formeduct.html', {"form": form,"id":id,"auth_user":request.user, "username": username})

def formExperience(request, id, username):
    if request.method == "POST":
        form = ExperienceForm(request.POST)
        if form.is_valid():
            user = auth_user.objects.get(username=username)
            cv = Cv.objects.get(user_id=user.id)
            cv.update_exp(
                id=id,
                company=form.cleaned_data['company'],
                job_title=form.cleaned_data['job_title'],
                start_date=form.cleaned_data['start_date'],
                end_date=form.cleaned_data['end_date'],
                description=form.cleaned_data['description']
            )
            return redirect('PNP:profile', username=request.user.username)
    else:
        cv = Cv.objects.get(user_id=request.user.id)
        experience = next((exp for exp in cv.experiences if exp['id'] == id), None)

        if experience is not None:
            form = ExperienceForm()
            form.fields['company'].initial = experience['company']
            form.fields['job_title'].initial = experience['job_title']
            form.fields['start_date'].initial = experience['start_date']
            form.fields['end_date'].initial = experience['end_date']
            form.fields['description'].initial = experience['description']

    return render(request, 'profilePage/formexp.html', {"form": form,"id":id,"auth_user":request.user, "username": username})
def delete_experience(request, id,username):
    cv = Cv.objects.get(user_id=request.user.id)
    cv.delete_experience(id)
    return render(request, 'profilePage/experience.html', {'isMe': request.user.username == username,'cv': cv})

def delete_education(request, id,username):
    cv = Cv.objects.get(user_id=request.user.id)
    cv.delete_education(id)
    return render(request, 'profilePage/education.html', {'isMe': request.user.username == username,'cv': cv})

def delete_skill(request, id,username):
    cv = Cv.objects.get(user_id=request.user.id)
    cv.delete_skills(id)
    cv.skills = json.loads(cv.skills)
    return render(request, 'profilePage/skills.html', {'isMe': request.user.username == username,'cv': cv})

def delete_language(request, id,username):
    cv = Cv.objects.get(user_id=request.user.id)
    cv.delete_languages(id)
    cv.languages = json.loads(cv.languages)
    return render(request, 'profilePage/langs.html', {'isMe': request.user.username == username,'cv': cv})


def chat(request, username):
    # get id of room that have <2 members and username in it
    room = Room.objects.filter(participent__user__username=username).annotate(participent_count=Count('participent')).filter(participent_count__lt=2).first()
    print(room)
    if room is None:
        # create a new room with the current user and the user with username
        user = auth_user.objects.get(username=username)
        userpnp= User.objects.get(user_id=user.id)
        current_user = User.objects.get(user_id=request.user.id)
        room = Room.create_discussion(current_user,userpnp.id)
    context = {
        'id': room.room_ID,
    }
    return render(request, 'messagePage/message/contentchat/content.html', context)
# metting pages

##metting choix page
def mettingPage(request):
    userRole = User.objects.get(user_id=request.user.id).role
    if userRole == 1:
        return redirect('PNP:joinMetting')
    return render(request,'messagePage/mettingPage.html' ,{'ismetting':True})


##metting create page
def metting(request):
    context = {
        'username': request.user.username,
        
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
    # get all rooms that i am a participents in it
    rooms = Room.objects.filter(participent=userInfo)

    room_with_participent=[{
        'room': room,
        'participent': room.participent.all().exclude(user_id=userID),
        'lastmessage': Message.objects.filter(room=room).last(),
    } for room in rooms]
    part = []

    context = {
        'rooms': room_with_participent,
        'auth_user': request.user,
        'ismessaging': True,
    }
    return render(request,'messagePage/messagePage.html' , context)

def roomCreateForm(request,type,id):
    context = {}
    print(request.method)
    if request.method == 'POST':
        if(type == 2):
            form = RoomForm(request.POST,request.FILES)
        elif(type == 3):
            form = AddMember(request.POST)
        else:
            form = DuscForm(request.POST)
        if form.is_valid():
            if type == 2:
                name = form.cleaned_data['name']
                if 'image' in form.files:
                    image = form.files['image']
                else:
                    image = None
                description = form.cleaned_data['description']
            participents = form.cleaned_data['participent']
            userpnp= User.objects.get(user_id=request.user.id)
            if type == 2:
                Room.create_room(userpnp,name, description,participents,image)
            elif type == 3:
                room = Room.objects.get(pk=id)
                for participent in participents:
                    room.add_participent(participent)
            else:
                Room.create_discussion(userpnp,participents)
            context.update({
                'success': True,
            })
            return redirect('PNP:messaging')
    else:
        participents = []
        user = User.objects.get(user_id=request.user.id)  # Get the current user
        part = user.friends.all().exclude(user_id=request.user.id)  # Get all friends of the user
        rooms = Room.objects.annotate(participent_count=Count('participent')).filter(participent_count__lt=2)
        i = 0
        for p in part:
            if rooms.filter(participent=p).exists():  # Check if the friend is a participant in any of these rooms
                participents.append(p)
        participent_ids = [p.id for p in participents]
        

        if type == 1:
            form = DuscForm()
            form.fields['participent'].queryset = User.objects.filter(id__in=participent_ids)
        elif type == 2:
            form = RoomForm()
            # get all rooms that participents is under 2 users 
            participents = user.friends.all().exclude(user_id=request.user.id)  # Get all friends of the user
            form.fields['participent'].queryset = User.objects.filter(id__in=[p.id for p in participents])
        else:
            form = AddMember()
            room = Room.objects.get(pk=id)
            paricipents_not_in_room = user.friends.all().exclude(id__in=room.participent.all())
            form.fields['participent'].queryset = User.objects.filter(id__in=paricipents_not_in_room)


    context.update({
        'form': form,
        'type': type,
        'id':id,
    })
    return render(request, 'messagePage/message/sideBar/form.html', context)

def getMessages(request, id):   
    room = Room.objects.get(pk=id)
    particepent = []
    part = room.participent.all()
    for p in part:
        if p.user_id != request.user.id:
            particepent.append(p)
    messages = Message.objects.filter(room=room).order_by('created_at')
    message_with_time_since = [{
        'message': message,
        'time_since': time_since(message.created_at),
    } for message in messages]
    context = {
        'messages': message_with_time_since,
        'id': id,
        'notFirst': True,
        'participents': particepent,
        'room':room,
        'user': User.objects.get(user_id=request.user.id),
        'isgroup': True if room.name is not None else False,
        'Menbers': room.participent.all(),
    }
    return render(request, 'messagePage/message/contentchat/messages.html', context)

def messageForm(request, id):
    if request.method == 'POST':
        room = Room.objects.get(pk=id)
        message = request.POST.get('message')
        user = User.objects.get(user_id=request.user.id)
        message = Message.objects.create(room=room, message=message, user=user)
        
        # Get list of uploaded files
        files = request.FILES.getlist('files')
        types = request.POST.getlist('type')

        # Iterate over each uploaded file
        for file, type in zip(files, types):
            # Create a new PostMedia instance for each file
            message_media = MessageMedia.objects.create(media=File(file), type=type)
            # Associate the PostMedia instance with the Post
            message.media.add(message_media)
    return render(request, 'messagePage/message/contentchat/formchat.html', {'id': id})

def quitterRoom(request, id):
    room = Room.objects.get(pk=id)
    user = User.objects.get(user_id=request.user.id)
    room.remove_participent(user)
    if room.participent.count() == 0:
        room.delete()
    return JsonResponse({'success': True})

def members(request, id):
    room = Room.objects.get(pk=id)
    particepent = []
    part = room.participent.all()
    for p in part:
        if p.user_id != request.user.id:
            particepent.append(p)
    context = {
        'room': room,
        'members':particepent
    }
    return render(request, 'messagePage/members.html', context)

# def addParticipent(request, id):
#     room = Room.objects.get(pk=id)
#     user = User.objects.get(user_id=request.user.id)
#     participents = request.POST.getlist('participent')
#     for participent in participents:
#         userpnp= User.objects.get(user_id=participent)
#         room.add_participent(userpnp)
#     return JsonResponse({'success': True})
#search for rooms

def searchRoom(request, roomname):
    userID = request.user.id
    userInfo = User.objects.get(user_id=userID)
    users = auth_user.objects.filter(username__startswith=roomname)
    pnpusers = User.objects.filter(user_id__in=users).all()
    rooms = Room.objects.filter(participent__in=pnpusers.values_list('id', flat=True))
    print(rooms)
    if roomname == 'x212x':
        
        # get all rooms that i am a participents in it
        rooms= Room.objects.filter(participent=userInfo)
        print(rooms)
    
    rooms_with_participent=[{
        'room': room,
        'participent': room.participent.all().exclude(user_id=userID),
        'lastmessage': Message.objects.filter(room=room).last(),
    } for room in rooms]


    return render(request,'messagePage/message/sideBar/disc.html' , {'rooms': rooms_with_participent})


# first page after login

def firstPage(request):
    users = User.objects.filter(Visibility='public')
    posts = Post.objects.filter(user_id__in=users)
    context = {}
    posts_with_time_since = [{
            'post': post,
            'time_since': time_since(post.created_at),
            'numberComments': Comment.objects.filter(object_id=post.id).count()
        } for post in posts]

    if request.user.is_authenticated:
        current_user = User.objects.get(user_id=request.user.id)
        friends = current_user.friends.all()
        segg = seggestedFriends(request)
        posts = Post.objects.filter(Q(user_id__in=friends) | Q(user_id=current_user.id)).order_by('-created_at')

        # check if the current user liked the post or not
        for post in posts:
            post.liked = Like.objects.filter(post_id=post.id, user_id=current_user.id).exists()
        posts_with_time_since = [{
            'post': post,
            'time_since': time_since(post.created_at),
            'numberComments': Comment.objects.filter(object_id=post.id).count()
        } for post in posts]

        rooms = Room.objects.filter(participent=current_user)
        context.update({
            'rooms': rooms,
            'segguestedFriends': segg,
            'user': current_user,
            'auth_user': request.user,
            'number_of_visits': current_user.number_of_profile_visits,
            'number_of_posts': Post.objects.filter(user_id=current_user.id).count(),
            'number_of_friends': current_user.friends.count(),
            'friends': friends,
        })

    context.update({
        'posts': posts_with_time_since,
        'ishome': True,
    })

    return render(request, 'firstPage/fisrtPage.html', context)


def addFriend(request,friend):
    user = auth_user.objects.get(username=friend)  # get User instance from User model
    friendpnp= User.objects.get(user_id=user.id)
    current_user = User.objects.get(user_id=request.user.id)

    # Check if they are already friends
    if current_user.friends.filter(user_id=user.id).exists():
        # If they are friends, remove the friend
        current_user.friends.remove(friendpnp)
    else:
        # If they are not friends, check if a friend request has been sent in either direction
        if FriendRequest.objects.filter(sender=current_user, receiver=friendpnp).exists() or FriendRequest.objects.filter(sender=friendpnp, receiver=current_user).exists():
            # If a friend request has been sent, delete it
            FriendRequest.objects.filter(sender=current_user, receiver=friendpnp).delete()
            FriendRequest.objects.filter(sender=friendpnp, receiver=current_user).delete()
            # And add the friend
        else:
            # If no friend request has been sent, send one if the friend's visibility is private
            if friendpnp.Visibility == "private":
                FriendRequest.objects.create(sender=current_user, receiver=friendpnp)
            else:
                # If the friend's visibility is public, add the friend
                current_user.friends.add(friendpnp)

    return render(request, 'profilePage/followBtn.html', {'friend':friend,'the_user': user, 'isMe': False, 'auth_user': request.user,'requestsend': FriendRequest.objects.filter(sender=current_user.id,receiver=friendpnp).exists(), 'isFriend': current_user.friends.filter(user_id=user.id).exists(),'is_private': friendpnp.Visibility == 'private'})


def seggestedFriends(request):
    user = User.objects.get(user_id=request.user.id)
    friends = user.friends.all()
    friends_request = FriendRequest.objects.filter(receiver=user.id)
    sent_request = FriendRequest.objects.filter(sender=user.id)
    all_users = User.objects.all()
    suggested_friends = []
    
    for u in all_users:
        if u != user and u not in friends and u not in sent_request and u not in friends_request:
            suggested_friends.append(u)
    # Take 7 random users
    if len(suggested_friends) > 7:
        suggested_friends = random.sample(suggested_friends, 7)
    
    suggested_friends = suggested_friends[:7]
    
    return suggested_friends


def accept_request(request, username):
    user = auth_user.objects.get(username=username)
    friend = User.objects.get(user_id=user.id)
    current_user = User.objects.get(user_id=request.user.id)
    current_user.friends.add(friend)
    FriendRequest.objects.get(sender=friend.id, receiver=current_user.id).delete()
    return redirect('PNP:profile', username=current_user.user.username)

def reject_request(request, username):
    user = auth_user.objects.get(username=username)
    friend = User.objects.get(user_id=user.id)
    current_user = User.objects.get(user_id=request.user.id)
    FriendRequest.objects.get(sender=friend.id, receiver=current_user.id).delete()
    return redirect('PNP:profile', username=current_user.user.username)

# create post

def get_posts(request):
    current_user = User.objects.get(user_id=request.user.id)
    friends = current_user.friends.all()
    posts = Post.objects.filter(Q(user_id__in=friends) | Q(user_id=current_user.id)).order_by('-created_at')

    # check if the current user liked the post or not
    for post in posts:
        post.liked = Like.objects.filter(post_id=post.id, user_id=current_user.id).exists()

    posts_with_time_since = [{
        'post': post,
        'time_since': time_since(post.created_at),
        'numberComments': Comment.objects.filter(object_id=post.id).count()
    } for post in posts]
    context = {
        'posts': posts_with_time_since,
        'auth_user': request.user,
    }
    return render(request, 'firstPage/posts.html', context)


def add_post(request):
    if request.method == 'POST':
        content = request.POST.get('postContent')
        auth_userid = request.user.id   
        user_id = User.objects.get(user_id=auth_userid).id
        post = Post.create_post(content, user_id)
        
        # Get list of uploaded files
        files = request.FILES.getlist('files')
        types = request.POST.getlist('type')

        # Iterate over each uploaded file
        for file, type in zip(files, types):
            # Create a new PostMedia instance for each file
            post_media = PostMedia.objects.create(media=File(file), type=type)
            # Associate the PostMedia instance with the Post
            post.media.add(post_media)
        
        print("post added")

    return JsonResponse({'success': True})

def deletePost(request, id):
    post = Post.objects.get(id=id)
    post.delete()
    pnp_user = User.objects.get(user_id=request.user.id)
    posts = Post.objects.filter(user_id=pnp_user.id).all().order_by('-created_at')
    for post in posts:
        post.liked = Like.objects.filter(post_id=post.id, user_id=pnp_user.id).exists()
    posts_with_time_since = [{
        'post': post,
        'time_since': time_since(post.created_at),
        'numberComments': Comment.objects.filter(object_id=post.id).count()
    } for post in posts]

    return render(request, 'profilePage/Post.html',{'posts': posts_with_time_since,'isMe': True,'auth_user': request.user})
    
#network page
def network(request):
    context = {
        'friends' : User.objects.get(user_id=request.user.id).friends.all().exclude(user_id=request.user.id),
        'auth_user': request.user,
        'isNetwork': True,
    }
    return render(request,'networkPage/networkPage.html' , context)

#classroom page
def classroom(request):
    user_cours = Cours.objects.all()
    print(user_cours)
    context = {
        
        'user_cours': user_cours,
    }
    if request.user.is_authenticated:
        context.update({
            'auth_user': request.user,
            'isClassroom': True,
        })
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
def get_comment(request, itemid):
    #clear session
    request.session['postId'] = None
    # type =1 for post and 2 for comment
    request.session['postId'] = itemid
    post = Post.objects.get(pk=itemid)
    comments = post.comments.all()

    #get all replies for eacxh comment
    context = {
        'comments': comments,

    }
    return render(request, 'firstPage/commentsFrom.html', context)
    
def showCommentForm(request, itemid,type):
    if(type == 1):
        item = Post.objects.get(pk=itemid)
        postId=itemid
    else:
        item = Comment.objects.get(pk=itemid)
        postId=request.session.get('postId')
    return render(request, 'firstPage/addComment.html', {'postId':postId,'itemId': itemid,'comment':item, 'type': type,'is_reply': False if type == 1 else True})

def addComment(request, itemid,type):
    if request.method == 'POST':
        content = request.POST.get('commentContent')
        user = User.objects.get(user_id=request.user.id)
        if type == 1:
            object = Post.objects.get(id=itemid)
        else:
            object = Comment.objects.get(id=itemid)
        request.session['type'] = type
        contentType = ContentType.objects.get_for_model(object)
        if type == 1:
            Comment.create_comment(user, itemid , content,contentType)
        else:
            object.create_reply(user, itemid , content,contentType)
        return redirect(request.path_info)
    request.session['postId'] = None
    return redirect('PNP:firstPage')


#seach
def search(request, username,type):
    # 0 for all 1 for students 2 for teachers 3 for companies
    if type == 0:
        authuser = auth_user.objects.filter(username__startswith=username)
        user = User.objects.filter(user_id__in=authuser)
        return render(request,'firstPage/search.html' , {'users': user})
    elif type == 1:
        authuser = auth_user.objects.filter(username__startswith=username)
        user = User.objects.filter(user_id__in=authuser).filter(role = 1)
        if username == 'x212x':
            user = User.objects.filter(role=1)
        return render(request,'firstPage/search.html' , {'users': user})
    elif type == 2:
        authuser = auth_user.objects.filter(username__startswith=username)
        user = User.objects.filter(user_id__in=authuser).filter(role = 2)
        if username == 'x212x':
            user = User.objects.filter(role=2)
        return render(request,'firstPage/search.html' , {'users': user})
    else:
        authuser = auth_user.objects.filter(username__startswith=username)
        user = User.objects.filter(user_id__in=authuser).filter(role = 3)
        if username == 'x212x':
            user = User.objects.filter(role=3)
        return render(request,'firstPage/search.html' , {'users': user})


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

from django.shortcuts import render, redirect
from .forms import CoursForm
from .models import Cours

def create_cours(request):
    print("DEBUG: Vue create_cours appelée.")
    if request.user.is_authenticated:  # Vérifie si l'utilisateur est connecté
        print(f"DEBUG: Utilisateur connecté : {request.user}")
        if request.method == 'POST':
            form = CoursForm(request.POST)
            if form.is_valid():
                new_cours = form.save(commit=False)
                new_cours.teacher = request.user
                if not new_cours.code:
                    new_cours.generate_code()
                new_cours.save()
                return redirect('/classroom')  
        else:
            form = CoursForm()
        return render(request, 'classroom/create_cours.html', {'form': form})
    else:
        print("DEBUG: Utilisateur non connecté. Redirection vers la page de connexion.")
        return redirect('login')  # Redirige vers la page de connexion si l'utilisateur n'est pas connecté
    
def ouvrir_pdf(request):
    nom_du_fichier = "Calendrier-universitaire-2023-2024.pdf"
    chemin_pdf = settings.STATIC_URL + 'PNP/pdfs/' + nom_du_fichier
    return JsonResponse({'url': chemin_pdf})
    
def rejoindre_cours(request):
    if request.method == 'POST':
        code = request.POST.get('code')  # Récupérer le code du cours depuis le formulaire
        try:
            cours = Cours.objects.get(code=code)  # Vérifier si un cours avec ce code existe
            
            cours.students.add(request.user)
            cours.save()
            return redirect('detail_cours', cours_id=cours.id)  # Rediriger vers la page du cours
            #return redirect('/classroom/detail_cours.html')
        except Cours.DoesNotExist:
            # Si le cours n'existe pas, renvoyez l'utilisateur à la même page avec un message d'erreur
            return render(request, 'classroom/rejoindre_cours.html', {'error_message': 'Code de cours invalide'})
    else:
        return render(request, 'classroom/rejoindre_cours.html')

    

 
def detail_cours(request, code):
    # Obtenir le cours correspondant au code fourni dans l'URL
    cours = get_object_or_404(Cours, code=code)
    # Obtenir la documentation associée à ce cours s'il y en a
    documentation = Documentation.objects.filter(cours=cours)

    # Passer les données à votre modèle de page HTML
    context = {
        'cours': cours,
        'documentation': documentation,
        'auth_user': request.user
    }

    return render(request, 'classroom/detail_cours.html', context)

def students_page(request, code):
    # Retrieve the specific course based on the code provided in the URL
    cours = get_object_or_404(Cours, code=code)

    # Retrieve the students associated with this course
    students = cours.students.all()

    # Retrieve the teacher associated with this course and their username
    teacher_username = cours.teacher.username

    context = {
        'students': students,
        'teacher_username': teacher_username,
        'cours': cours
    }

    # Render the HTML page with the real student and teacher data, along with course data
    return render(request, 'classroom/students_page.html', context)

def mes_cours(request):
    # Récupérer les cours créés par l'utilisateur actuellement connecté
    cours_utilisateur = Cours.objects.filter(teacher=request.user)
    context = {'cours_utilisateur': cours_utilisateur}
    return render(request, 'classroom/myCourses.html', context)


def travaux_et_devoir(request, code):
    cours = get_object_or_404(Cours, code=code)

    devoirs = Devoir.objects.filter(cours=cours)
    # Vous pouvez passer ces données à votre modèle de page HTML
    context = {
        'devoirs': devoirs,  # Utilisation de la variable devoirs plutôt que travaux_et_devoir_list
        'cours': cours,
        'auth_user': request.user  # Ajout de l'utilisateur actuel à context
    }

    # Renvoyez une réponse HTTP avec le modèle rendu contenant les travaux et devoirs
    return render(request, 'classroom/Travaux&Devoir.html', context)




def creer_devoir(request, code):
    cours = get_object_or_404(Cours, code=code)  # Récupérer l'instance de Cours correspondant au code passé dans l'URL
    form = DevoirForm(request.POST, request.FILES)
    if form.is_valid():
            devoir = form.save(commit=False)
            devoir.cours = cours
            devoir.save()
            return redirect('/classroom/detail_cours/{}/travaux_et_devoir/'.format(code))


    else:
        # Si la requête est GET, afficher le formulaire vide
        form = DevoirForm()

    return render(request, 'classroom/creer_devoir.html', {'form': form})

def creer_documentation(request, code):
    cours = get_object_or_404(Cours, code=code)  # Récupérer l'instance de Cours correspondant au code passé dans l'URL
    form = DocumentationForm(request.POST, request.FILES)
    if form.is_valid():
            documentation = form.save(commit=False)
            documentation.cours = cours
            documentation.save()
            return redirect('/classroom/detail_cours/{}/travaux_et_devoir/'.format(code))


    else:
        # Si la requête est GET, afficher le formulaire vide
        form = DocumentationForm()
    return render(request, 'classroom/creer_documentation.html', {'form': form})

#search Page
def searchPage(request):
    return render(request, 'searchPa/searchPage.html', {'auth_user': request.user,'isSearch': True})