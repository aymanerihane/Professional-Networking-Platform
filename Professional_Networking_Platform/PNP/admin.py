from django.contrib import admin

from .models import User, Post

admin.site.register(Post)
admin.site.register(User)

# Register your models here.
