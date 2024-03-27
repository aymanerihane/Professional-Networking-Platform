from django.db import models
from django.core.validators import URLValidator
from django.contrib.contenttypes.fields import GenericRelation
###########
# Post Model

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.TextField()
    num_comments  = models.PositiveIntegerField(default=0)
    num_shares = models.PositiveIntegerField(default=0)
    num_likes  = models.PositiveIntegerField(default=0)
    #
    media = models.ManyToManyField('PNP.PostMedia', related_name='posts', blank=True)
    #
    comments= GenericRelation('PNP.Comment')
    #
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #
    user = models.ForeignKey('PNP.User', on_delete=models.CASCADE)
    #

    ###############

    ######## CRUD operations

    ## Create operation
    def create_post(content, user_id):
        post = Post.objects.create(
            content=content,
            user_id=user_id,
            
        )
        return post

    #### Read operation :

    ## Get all posts
    def get_all_posts():
        return Post.objects.all()

    ## Get a specific post by ID
    def get_post_by_id(post_id):
        try:
            return Post.objects.get(pk=post_id)
        except Post.DoesNotExist:
            return None

    ## Update operation
    def update_post(self,post_id, title=None, description=None, location=None, link=None, media=None):
        post = self.get_post_by_id(post_id)
        if post:
            if title:
                post.title = title
            if description:
                post.description = description
            if location:
                post.location = location
            if link:
                post.link = link
            if media:
                post.media = media
            post.save()
            return post
        else:
            return None
        

    ## Delete operation
    def delete_post(self,post_id):
        post = self.get_post_by_id(post_id)
        if post:
            post.delete()
            return True
        else:
            return False
        
    def __str__(self):
        return self.title + ' - ' + self.user.user.username
