from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


def post_upload_images(obj):
    return mark_safe('<a href="{}">Форма загрузки</a>'.format(
        reverse('core:admin_upload_images', args=[obj.id])))


@admin.register(Models)
class ModelsAdmin(admin.ModelAdmin):
    list_display = ['name', 'image']
    list_filter = ['name']
    prepopulated_fields = {'slug': ('name',)}
    exclude = ['stars']


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['post', 'image',  'for_title']
    list_filter = ['post']
    list_editable = ['for_title']
    exclude = ['likes']



class ImageInLine(admin.StackedInline):
    model = Image
    raw_id_fields = ("post",)
    exclude = ['likes']


@admin.register(CosplayPost)
class CosplayPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'rubric', 'recommended', post_upload_images]
    list_filter = ['title', 'rubric', 'recommended']
    list_editable = ['recommended']
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ImageInLine, ]


@admin.register(CosplayRubric)
class CosplayRubricAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_filter = ['title']
    prepopulated_fields = {'slug': ('title',)}
