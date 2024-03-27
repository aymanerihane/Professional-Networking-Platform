from django.db import models

class PostMedia(models.Model):
    media = models.ImageField(upload_to='post/', null=True, blank=True)
    type = models.PositiveSmallIntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
