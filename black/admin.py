from django.contrib import admin

from black.models import Posts,Comment,Information,Buys,Img,Answer
# Register your models here.

admin.site.register([Posts,Comment,Information,Buys,Img,Answer])