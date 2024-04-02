from django.contrib import admin

from .models import User, Post, Comment,Class,Teacher,Student,Entreprise

admin.site.register(Class)
admin.site.register(Comment)
admin.site.register(Post)
admin.site.register(Entreprise)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(User)


# Register your models here.
