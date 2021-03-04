from django.db import models
from django.urls import reverse
from easy_thumbnails.fields import ThumbnailerImageField
from django.template.defaultfilters import slugify
from apps.account.models import User
from config import settings
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType


def upload_path_image(instance, filename):
    return 'images/{0}/{1}/{2}'.format(instance.collection.model, instance.collection.title, filename)


def upload_path_model_photo(instance, filename):
    return 'images/{0}/profile/{1}'.format(instance, filename)


class Models(models.Model):
    """ Наши модели"""
    name = models.CharField('Имя', max_length=30, blank=True)
    image = ThumbnailerImageField('Фото', upload_to=upload_path_model_photo, blank=True)
    stars = models.ManyToManyField(User, related_name='stars')
    slug = models.SlugField(max_length=200, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Создан')

    class Meta:
        ordering = ('id',)
        verbose_name = "Модель"
        verbose_name_plural = "Модели"

    def __str__(self):
        return str(self.name)

    def collections_by_model(self):
        collections = Image_Collection.objects.filter(model=self)
        return collections

    @property
    def total_stars(self):
        return self.stars.count()

    def get_absolute_url(self):
        return reverse('core:model_profile', args=[self.slug])


class CosplayRubric(models.Model):
    """ Темы коллекций изображений"""
    title = models.CharField('Наименование темы', max_length=50, blank=True)
    slug = models.SlugField(max_length=200, blank=True)

    class Meta:
        ordering = ('id',)
        verbose_name = "Рубрика"
        verbose_name_plural = "Рубрики"

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return reverse('core:collections_by_rubric', args=[self.slug])


class Image_Collection(models.Model):
    """ Коллекция изображений"""
    model = models.ForeignKey(Models, related_name='model_collections', on_delete=models.CASCADE)
    rubric = models.ForeignKey(CosplayRubric, related_name='collections', on_delete=models.CASCADE)
    title = models.CharField('Наименование коллекции', max_length=50, blank=True)
    description = models.CharField('Описание коллекции', max_length=300, blank=True)
    slug = models.SlugField(max_length=200, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Создан')

    class Meta:
        ordering = ('id',)
        verbose_name = "Коллекция"
        verbose_name_plural = "Коллекции"

    def __str__(self):
        return str(self.title)

    def images_in_collection(self):
        images = Image.objects.filter(collection=self)
        return images


class Image(models.Model):
    """ Изображение"""
    collection = models.ForeignKey(Image_Collection, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='likes')
    title = models.CharField('Наименование изображения', max_length=50, blank=True)
    slug = models.SlugField(max_length=200, blank=True)
    image = ThumbnailerImageField(upload_to=upload_path_image, blank=True, verbose_name='Изображение')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Создан')

    class Meta:
        ordering = ('id',)
        verbose_name = "Изображение"
        verbose_name_plural = "изображения"

    def __str__(self):
        return str(self.title)

    @property
    def total_likes(self):
        return self.likes.count()


class CosplayBlogPost(models.Model):
    """ Посты в единственный блог"""
    collections = models.ManyToManyField(Image_Collection)
    title = models.CharField('Наименование поста', max_length=50, blank=True)
    slug = models.SlugField(max_length=200, blank=True)
    description = models.CharField('Описание', max_length=500, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Создан')

    class Meta:
        ordering = ('id',)
        verbose_name = "Пост"
        verbose_name_plural = "Посты"

    def __str__(self):
        return str(self.title)


class ImageComment(models.Model):
    """ Комментарии к изображению """
    text = models.CharField('Текст комментария', max_length=500, blank=True)
    image = models.ForeignKey(Image, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    updated = models.BooleanField(default=False)

    class Meta:
        ordering = ('id',)
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

    def __str__(self):
        return str(self.text)


