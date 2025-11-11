from django.contrib import admin

from posts.models import Image


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('id','image')
