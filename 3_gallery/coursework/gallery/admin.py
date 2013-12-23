# -*- coding: utf-8 -*-


from django.contrib import admin
from gallery.models import *


class ImageAdmin(admin.ModelAdmin):
    list_display = ['image', 'preview_image_url', 'title', 'dsc']
    list_display_links = ['image', 'title']
    orderring = ['title']


admin.site.register(Image, ImageAdmin)
