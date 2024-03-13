from django.db import models

class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey('PNP.User', on_delete=models.CASCADE)
    post_id = models.ForeignKey('PNP.Post', on_delete=models.CASCADE)
    #
    comment = models.TextField()
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
