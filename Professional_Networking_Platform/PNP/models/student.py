from django.db import models
from .users import User
from .classe import Class


#################
# Student model #
class Student(models.Model): 
    CNE = models.AutoField(primary_key=True)
    parcours = models.TextField(default='[]') # JSON Array
    #
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    class_id = models.ForeignKey('PNP.Class', on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
