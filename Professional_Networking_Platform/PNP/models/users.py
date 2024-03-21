from django.db import models
from django import forms
from django.http import HttpResponse
from django.contrib.auth.models import User as auth_user


#################
# User model #

class User(models.Model):
    
    
    user = models.OneToOneField(auth_user, on_delete=models.CASCADE)
    # forms.py
    ROLE_CHOICES = [
        (1, 'Student'),
        (2, 'Teacher'),
        (3, 'Entreprise')
    ]

    VISIBILITY_CHOICES = [
        ('public', 'Public'),
        ('private', 'Private'),
    ]
    role = models.IntegerField(choices=ROLE_CHOICES,default=2) # 1: teacher, 2: student
    #
    #
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    #
    cv = models.FileField(upload_to='media/cv/',default='cv_default.jpg', null=True, blank=True)
    photo_profile = models.FileField(upload_to='media/avatar/',default='pdp_default.jpg', null=True, blank=True)
    #
    Visibility = models.CharField(max_length=10, choices=VISIBILITY_CHOICES, default='public')
    #
    #liste of rooms that the user is a member of
    rooms = models.ManyToManyField('PNP.Room',related_name='users', blank=True)
    #liste of friends
    friends = models.ManyToManyField('self',related_name='friends', blank=True)
    #
    number_of_profile_visits = models.PositiveIntegerField(default=0, blank=True, null=True)
    #
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username


