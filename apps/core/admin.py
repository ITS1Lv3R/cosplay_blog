from django.contrib import admin
from .models import *


@admin.register(Models)
class ModelsAdmin(admin.ModelAdmin):
    list_display = ['name', 'image']
    list_filter = ['name']
    prepopulated_fields = {'slug': ('name',)}
    exclude = ['stars']


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['post', 'rubric', 'image',  'for_title']
    list_filter = ['post']
    list_editable = ['for_title']
    exclude = ['likes']


class ImageInLine(admin.StackedInline):
    model = Image
    raw_id_fields = ("post",)
    exclude = ['likes']


@admin.register(CosplayPost)
class CosplayPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'rubric', 'recommended']
    list_filter = ['title', 'rubric', 'recommended']
    list_editable = ['recommended']
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ImageInLine, ]


@admin.register(CosplayRubric)
class CosplayRubricAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_filter = ['title']
    prepopulated_fields = {'slug': ('title',)}
