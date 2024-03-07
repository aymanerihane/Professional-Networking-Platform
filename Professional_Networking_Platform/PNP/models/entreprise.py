from django.db import models


###########
# entreprise modeles

class Entreprise(models.Model):
    ICE= models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    #
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #
    user = models.ForeignKey('PNP.User', on_delete=models.CASCADE)
    #