from django.db import models
from .Cours import Cours

class Devoir(models.Model):
    cours = models.ForeignKey(Cours, on_delete=models.CASCADE )
    titre = models.CharField(max_length=100)
    description = models.TextField()
    fichier_joint = models.FileField(upload_to='creer/devoir/', blank=True, null=True)
    date_limite = models.DateTimeField()


    def __str__(self):
        return self.titre

    def get_devoirs_by_code(code_cours):
        return Devoir.objects.filter(cours__code=code_cours)