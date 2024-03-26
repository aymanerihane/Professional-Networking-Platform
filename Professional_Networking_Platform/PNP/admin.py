from django.contrib import admin

from .models import User, Post, Comment,Class,Teacher

admin.site.register(Post)
admin.site.register(User)
admin.site.register(Comment)
admin.site.register(Class)
admin.site.register(Teacher)


# Register your models here.
