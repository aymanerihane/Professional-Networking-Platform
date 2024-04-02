from django.db import models
from .users import User

#################
# Teacher model #
class Teacher(models.Model):
    id = models.AutoField(primary_key=True)
    matricule = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #
    speciality = models.CharField(max_length=100)
    #
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @classmethod
    def create_teacher(self, user,matricule, speciality=None):
        teacher = self(user=user,matricule=matricule, speciality=speciality)
        teacher.save()
        return teacher
    
    def __str__(self):
        return self.matricule+ '-' + self.user.user.username