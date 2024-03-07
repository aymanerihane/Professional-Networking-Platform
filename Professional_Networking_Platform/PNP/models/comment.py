from django.db import models

class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey('PNP.User', on_delete=models.DO_NOTHING)
    post_id = models.ForeignKey('PNP.Post', on_delete=models.DO_NOTHING)
    #
    comment = models.TextField()
    #
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)