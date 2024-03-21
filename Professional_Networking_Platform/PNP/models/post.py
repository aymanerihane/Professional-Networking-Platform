from django.db import models
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

###########
# Post Model

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    num_comments  = models.PositiveIntegerField(default=0)
    num_shares = models.PositiveIntegerField(default=0)
    num_likes  = models.PositiveIntegerField(default=0)
    link = models.CharField(max_length=100, validators=[URLValidator()])
    media = models.FileField(upload_to='media/', null=True, blank=True)
    #
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #
    user = models.ForeignKey('PNP.User', on_delete=models.CASCADE)
    #

    ###############

    ######## CRUD operations

    ## Create operation
    def create_post(title, description, user_id, location=None, link=None, media=None):
        post = Post.objects.create(
            title=title,
            description=description,
            user_id=user_id,
            location=location,
            link=link,
            media=media
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
