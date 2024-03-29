from django.db import models
from django.contrib.auth.models import User
import random
import string



class Cours(models.Model):
   # id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, default='')
    class_name = models.CharField(max_length=100, default='')
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name='teacher', editable=False)
    salle = models.CharField(max_length=50, default='')
    subject = models.CharField(max_length=100, default='')
    code = models.CharField(max_length=10, unique=True, blank=True, editable=False)
    #student=models.ForeignKey(User, on_delete=models.CASCADE, related_name='student', editable=False)
    students = models.ManyToManyField(User, related_name='student', blank=True, editable=False)

    def get_teacher_username(self):
        return self.teacher.username

    def get_students_usernames(self):
        return [student.username for student in self.students]
    

    def generate_code(self):
        characters = string.ascii_uppercase + string.digits
        code = ''.join(random.choice(characters) for _ in range(6))  # Génère un code aléatoire de longueur 6
        self.code = code
    
    
   # Surcharge de la méthode save pour affecter automatiquement le nom d'utilisateur du professeur et générer un code
    def save(self, *args, **kwargs):
        # Si le champ teacher_id est vide, cela signifie que le modèle n'a pas encore été sauvegardé
        if not self.teacher_id:
            # Affecte le nom d'utilisateur du professeur au champ teacher_id
            self.teacher_id = self.teacher.username
        # Si le champ code est vide, cela signifie que le modèle n'a pas encore de code généré
        if not self.code:
            # Génère un code aléatoire et l'affecte au champ code
            self.generate_code()
        # Appelle la méthode save de la classe parente pour effectuer la sauvegarde
        super().save(*args, **kwargs)
        
        
      
    def __str__(self):
        return self.name