from django.db import models
from .teacher import Teacher


#################
# Class model #
class Class(models.Model):
    id = models.AutoField(primary_key=True)
    Name= models.CharField(max_length=100, default='')
    Degree = models.TextField(max_length=100, default='')
    
    #
   # teacher_id = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    #
    #
   # schedule_exams = models.TextField(default='[]')
    #
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)