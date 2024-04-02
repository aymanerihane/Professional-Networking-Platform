from django.db import models
from .users import User


#################
# Student model #
class Student(models.Model): 
    CNE = models.CharField(primary_key=True, max_length=100, unique=True)
    #
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    class_id = models.ForeignKey('PNP.Class', on_delete=models.DO_NOTHING, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @classmethod
    def create_student(self, user,cne, class_id=None):
        student = self(user=user,CNE=cne, class_id=class_id)
        student.save()
        return student
    
    def __str__(self):
        return self.CNE+ '-' + self.user.user.username