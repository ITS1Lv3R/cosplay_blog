from django.contrib import admin
from .models import *


@admin.register(Models)
class ModelsAdmin(admin.ModelAdmin):
    list_display = ['name', 'image']
    list_filter = ['name', ]
    prepopulated_fields = {'slug': ('name',)}
    exclude = ['stars']


class ImageInLine(admin.StackedInline):
    model = Image
    raw_id_fields = ("collection",)
    exclude = ['likes']


@admin.register(Image_Collection)
class Image_CollectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'model', 'description']
    list_filter = ['model', 'title']
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ImageInLine, ]


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['title', 'collection', 'image', ]
    list_filter = ['collection', 'title']
    prepopulated_fields = {'slug': ('title',)}
    exclude = ['likes']


@admin.register(CosplayBlogPost)
class CosplayBlogPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']
    list_filter = ['title']
    prepopulated_fields = {'slug': ('title',)}


@admin.register(ImageComment)
class ImageCommentAdmin(admin.ModelAdmin):
    list_display = ['text', 'created', 'updated']
    list_filter = ['text']


@admin.register(CosplayRubric)
class CosplayRubricAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_filter = ['title']
    prepopulated_fields = {'slug': ('title',)}
