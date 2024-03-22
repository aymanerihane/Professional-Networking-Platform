from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User as auth_user

class Comment(models.Model):
    object_id = models.PositiveSmallIntegerField()
    user_id = models.ForeignKey('PNP.User', on_delete=models.CASCADE)
    #
    comment = models.TextField()
    #
    content_type= models.ForeignKey(ContentType, on_delete=models.CASCADE)
    content_object = GenericForeignKey('content_type', 'object_id')
    #
    replies= GenericRelation('Comment')
    number_of_replies = models.PositiveIntegerField(default=0)
    number_of_likes = models.PositiveIntegerField(default=0)
    #
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # CRUD operations

    # Create operation
    def create_comment(user_id, post_id, comment_text):
        comment = Comment.objects.create(
            user_id=user_id,
            post_id=post_id,
            comment=comment_text
        )
        return comment

    # Read operation - Get all comments for a specific post
    def get_comments_for_post(post_id):
        return Comment.objects.filter(post_id=post_id)

    # Read operation - Get a specific comment by ID
    def get_comment_by_id(comment_id):
        try:
            return Comment.objects.get(pk=comment_id)
        except Comment.DoesNotExist:
            return None

    # Update operation
    def update_comment(self,comment_id, new_comment_text):
        comment = self.get_comment_by_id(comment_id)
        if comment:
            comment.comment = new_comment_text
            comment.save()
            return comment
        else:
            return None

    # Delete operation
    def delete_comment(self,comment_id):
        comment = self.get_comment_by_id(comment_id)
        if comment:
            comment.delete()
            return True
        else:
            return False


    def __str__(self):
        user= auth_user.objects.get(id=self.user_id.user_id)
        return user.username + " - " + self.comment