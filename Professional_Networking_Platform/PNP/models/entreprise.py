from django.db import models


###########
# entreprise modeles

class Entreprise(models.Model):
    ICE= models.CharField(max_length=100)
    #
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #
    user = models.ForeignKey('PNP.User', on_delete=models.DO_NOTHING)
    #

    @classmethod
    def create_entreprise(self, user, ice):
        entreprise = Entreprise.objects.create(
            ICE=ice,
            user=user
        )
        return entreprise
    
    def __str__(self):
        return self.ICE