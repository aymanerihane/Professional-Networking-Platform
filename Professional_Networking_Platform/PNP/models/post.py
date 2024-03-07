from django.db import models

###########
# Post Model

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    comments = models.TextField('[]')
    shares= models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    location = models.CharField(max_length=100)
    link = models.CharField(max_length=100)
    media = models.FileField(upload_to='media/', null=True, blank=True)
    #
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #
    user = models.ForeignKey('PNP.User', on_delete=models.CASCADE)
    #

