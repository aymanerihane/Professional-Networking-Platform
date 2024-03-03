from django.db import models
from .teacher import Teacher


#################
# Class model #
class Class(models.Model):
    id = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=100)
    Description = models.TextField()
    etudiants_id = models.TextField('[]') 
    teacher_id = models.ForeignKey(Teacher, on_delete=models.DO_NOTHING)
    #
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)