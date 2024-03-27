from django.db import models

class Like(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey('PNP.User', on_delete=models.CASCADE)
    post_id = models.ForeignKey('PNP.Post', on_delete=models.CASCADE)
    #
    #
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # CRUD operations

    def create_like(user_id, post_id):
        like, created = Like.objects.get_or_create(user_id=user_id, post_id=post_id)
        if created:
            post_id.save()

    def read_likes_for_post(post_id):
        return Like.objects.filter(post_id=post_id)

    def delete_like(user_id, post_id):
        try:
            like = Like.objects.get(user_id=user_id, post_id=post_id)
            post_id.save()
            like.delete()
        except Like.DoesNotExist:
            pass