from django.db import models
from .Cours import Cours

class Documentation(models.Model):
    cours = models.ForeignKey(Cours, on_delete=models.CASCADE)
    titre = models.CharField(max_length=100)
    description = models.TextField()
    fichier_joint = models.FileField(upload_to='documentation/', blank=True, null=True)

    def __str__(self):
        return self.titre