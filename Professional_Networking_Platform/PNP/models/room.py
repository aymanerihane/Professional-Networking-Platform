from django.db import models

class Room(models.Model):
    room_ID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    participent = models.ManyToManyField('PNP.User')
    #
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def create_room(user, name, description,participents):
        room = Room.objects.create(
            name=name,
            description=description            
        )
        room.add_participent(user)
        for participent in participents:
            room.add_participent(participent)
        room.save()

    def add_participent(self, user):
        self.participent.add(user)
        self.save()

    
