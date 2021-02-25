from django.contrib import admin
from .models import *


class ModelsAdmin(admin.ModelAdmin):
    list_display = ['name', 'image', 'stars_count']
    list_filter = ['stars_count']
    prepopulated_fields = {'slug': ('name',)}


class Image_CollectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'model']
    list_filter = ['model', 'title']
    prepopulated_fields = {'slug': ('title',)}


class ImageAdmin(admin.ModelAdmin):
    list_display = ['title', 'collection', 'image', 'description']
    list_filter = ['collection', 'title']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Models, ModelsAdmin)
admin.site.register(Image_Collection, Image_CollectionAdmin)
admin.site.register(Image, ImageAdmin)
