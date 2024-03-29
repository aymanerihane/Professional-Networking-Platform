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

    def create_entreprise(self, user, ICE):
        entreprise = Entreprise.objects.create(
            ICE=ICE,
            user=user
        )
        return entreprise