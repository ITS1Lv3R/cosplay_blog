from django.contrib import admin
from .models import *


@admin.register(Models)
class ModelsAdmin(admin.ModelAdmin):
    list_display = ['name', 'image', 'stars_count']
    list_filter = ['stars_count']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Image_Collection)
class Image_CollectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'model']
    list_filter = ['model', 'title']
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['title', 'collection', 'image', 'description']
    list_filter = ['collection', 'title']
    prepopulated_fields = {'slug': ('title',)}


@admin.register(CosplayBlogPost)
class CosplayBlogPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']
    list_filter = ['title']
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['text', 'created', 'updated']
    list_filter = ['text']


@admin.register(CosplayTheme)
class CosplayThemeAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_filter = ['title']
    prepopulated_fields = {'slug': ('title',)}




