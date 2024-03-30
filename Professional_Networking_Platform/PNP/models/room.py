from django.db import models

class Room(models.Model):
    room_ID = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to='groups/', blank=True, null=True)
    name = models.CharField(max_length=100, unique=True, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    participent = models.ManyToManyField('PNP.User')
    #
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def create_room(user, name, description,participents,image):
        room = Room.objects.create(
            name=name,
            description=description,   
            image=image   
        )
        room.add_participent(user)
        for participent in participents:
            room.add_participent(participent)
        room.save()

    def create_discussion(user,participents):
        room = Room.objects.create(
            name=None,
            description=None,
        )
        room.add_participent(user)
        room.add_participent(participents)
        room.save()

    def add_participent(self, user):
        self.participent.add(user)
        self.save()
    

    def remove_participent(self, user):
        print(self.participent.all())  # Print out the participants before
        self.participent.remove(user)
        self.save()
        print(self.participent.all())  # Print out the participants after
            
    def __str__(self) -> str:
        if self.name == None:
            return "Room "+str(self.room_ID)
        return self.name

    
