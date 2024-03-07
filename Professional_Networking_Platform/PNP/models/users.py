from django.db import models

#################
# User model #
class User(models.Model):
    id = models.AutoField(primary_key=True)
    role = models.IntegerField() # 1: teacher, 2: student
    #
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    #
    password = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    #
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    #
    cv = models.FileField(upload_to='cv/', null=True, blank=True)
    photo_profile = models.FileField(upload_to='photo_profile/', null=True, blank=True)
    #
    Visibility = models.BooleanField(default=True)
    #
    #liste of rooms that the user is a member of
    rooms = models.ManyToManyField('PNP.Room')
    #
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
