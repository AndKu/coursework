# -*- coding: utf-8 -*-


from django.contrib import admin
from gallery.models import *


class ImageAdmin(admin.ModelAdmin):
    admin.site.disable_action('delete_selected')
    def full_delete_selected(self, request, obj):
        for o in obj.all():
            o.delete()
    full_delete_selected.short_description = 'Удалить выбранные изображения'
    actions = ['full_delete_selected']
    list_display = ['image', 'preview_image_url', 'title', 'dsc']
    list_display_links = ['image', 'title']
    orderring = ['title']


admin.site.register(Image, ImageAdmin)
