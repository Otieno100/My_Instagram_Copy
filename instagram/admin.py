from django.contrib import admin
from django.contrib import admin
from .models import     Profile,Images,comments,likes
# Register your models here.
admin.site.register(Profile)
admin.site.register(Images)
admin.site.register(comments)
admin.site.register(likes)