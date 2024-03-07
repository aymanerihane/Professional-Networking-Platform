from django.db import models

class Like(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey('PNP.User', on_delete=models.DO_NOTHING)
    post_id = models.ForeignKey('PNP.Post', on_delete=models.DO_NOTHING)
    #
    number_of_likes = models.IntegerField()
    #
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)