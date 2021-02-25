from django.db import models
from easy_thumbnails.fields import ThumbnailerImageField


def upload_path_image(instance, filename):
    return 'images/{0}/{1}/{2}'.format(instance.collection.model, instance.collection.title, filename)


def upload_path_model_photo(instance, filename):
    return 'images/{0}/profile/{1}'.format(instance, filename)


class Models(models.Model):
    """ Наши модели"""
    name = models.CharField('Имя', max_length=30, blank=True)
    image = ThumbnailerImageField('Фото', upload_to=upload_path_model_photo, blank=True)
    slug = models.SlugField(max_length=200, blank=True)
    stars_count = models.IntegerField('Количество звёзд у модели', null=True, default=1)
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


class Image_Collection(models.Model):
    """ Коллекция изображений"""
    model = models.ForeignKey(Models, related_name='collections', on_delete=models.CASCADE)
    title = models.CharField('Наименование коллекции', max_length=50, blank=True)
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
    title = models.CharField('Наименование изображения', max_length=50, blank=True)
    slug = models.SlugField(max_length=200, blank=True)
    image = ThumbnailerImageField(upload_to=upload_path_image, blank=True, verbose_name='Изображение')
    description = models.CharField('Описание изображения', max_length=300, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Создан')

    class Meta:
        ordering = ('id',)
        verbose_name = "Изображение"
        verbose_name_plural = "изображения"

    def __str__(self):
        return str(self.title)
