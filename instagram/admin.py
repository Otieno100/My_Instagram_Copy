from django.contrib import admin
from django.contrib import admin
from .models import     Profile,Image,comments,likes
# Register your models here.
admin.site.register(Profile)
admin.site.register(Image)
admin.site.register(comments)
admin.site.register(likes)