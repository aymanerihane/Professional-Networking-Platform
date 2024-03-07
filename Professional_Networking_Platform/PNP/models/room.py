from django.db import models

class Room(models.Model):
    room_ID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    #
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    
