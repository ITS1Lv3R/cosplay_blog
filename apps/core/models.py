from django.db import models
from django.urls import reverse
from easy_thumbnails.fields import ThumbnailerImageField
from django.template.defaultfilters import slugify
from apps.account.models import User
from config import settings
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.core.validators import RegexValidator, MinLengthValidator


def upload_path_image(instance, filename):
    return 'images/{0}/{1}/{2}'.format(instance.post.model, instance.post.rubric, filename)


def upload_path_model_photo(instance, filename):
    return 'images/{0}/profile/{1}'.format(instance, filename)


class Models(models.Model):
    """ Наши модели"""
    name = models.CharField('Имя', max_length=30, blank=True)
    image = ThumbnailerImageField('Фото', upload_to=upload_path_model_photo, blank=True)
    stars = models.ManyToManyField(User, related_name='models')
    slug = models.SlugField(max_length=200, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Создан')

    class Meta:
        ordering = ('id',)
        verbose_name = "Модель"
        verbose_name_plural = "Модели"

    def __str__(self):
        return str(self.name)

    def posts_by_model(self):
        posts = CosplayPost.objects.filter(model=self)
        return posts

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
        return reverse('core:posts_by_rubric', args=[self.slug])

    def posts_by_rubric(self):
        posts = CosplayPost.objects.filter(rubric=self)
        return posts

    def image_for_title(self):
        try:
            post = CosplayPost.objects.filter(rubric=self).first()
            image_for_title = post.image_for_title()
        except:
            image_for_title = 'static/img/vk.png'

        return image_for_title


class CosplayPost(models.Model):
    """ Посты в единственный блог"""
    model = models.ForeignKey(Models, related_name='models', on_delete=models.CASCADE)
    rubric = models.ForeignKey(CosplayRubric, related_name='posts', on_delete=models.CASCADE)
    title = models.CharField('Наименование поста', max_length=60, blank=True,
                             validators=[MinLengthValidator(40,
                                                            message='Length has to be a minimum 40')])
    slug = models.SlugField(max_length=200, blank=True)
    description = models.CharField('Описание', max_length=9999, blank=True)
    recommended = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Создан')

    class Meta:
        ordering = ('id',)
        verbose_name = "Пост"
        verbose_name_plural = "Посты"

    def __str__(self):
        return str(self.title)

    def images_in_post(self):
        images = Image.objects.filter(post=self)
        return images

    def image_for_title(self):
        image_for_title = Image.objects.filter(post=self, for_title=True).first()
        return image_for_title

    def get_absolute_url(self):
        return reverse('core:post_view', args=[self.slug])


class Image(models.Model):
    """ Изображение"""
    post = models.ForeignKey(CosplayPost, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='likes')
    image = ThumbnailerImageField(upload_to=upload_path_image, blank=True, verbose_name='Изображение')
    for_title = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Создан')

    class Meta:
        ordering = ('id',)
        verbose_name = "Изображение"
        verbose_name_plural = "изображения"

    def __str__(self):
        return str(self.post)

    @property
    def total_likes(self):
        return self.likes.count()

    def get_absolute_url(self):
        return reverse('core:image_view', args=[self.pk])

