from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from apps.core.models import Models, CosplayBlogPost, Image, CosplayTheme


def index(request):
    """ Главная страница со списком всех постов"""
    posts = CosplayBlogPost.objects.all()
    return render(request, 'core/index.html', {'posts': posts})


def models_list(request):
    """ список всех моделей"""
    models = Models.objects.all()
    return render(request, 'core/models/models_list.html', {'models': models})


def model_profile(request, slug):
    """ Профиль выбранной модели"""
    response_message = 'Все коллекции модели: '
    model = Models.objects.get(slug=slug)
    # достаём все коллеции у выбранной модели
    collections = model.collections_by_model()
    if not collections:
        response_message = 'У данной модели нет коллекций'
    context = locals()
    return render(request, 'core/models/model_profile.html', context)


class ImageView(DetailView):
    """ Детальная вью для изображений"""
    model = Image
    queryset = Image.objects.all()
    template_name = 'core/image_view.html'
    context_object_name = 'image'


class ThemeView(ListView):
    """ Список всех тематик"""
    model = CosplayTheme
    queryset = CosplayTheme.objects.all()
    template_name = 'core/themes/themes_list.html'
    context_object_name = 'themes'


def collections_by_theme(request, slug):
    """ Страница с коллекциями по темам"""
    theme = CosplayTheme.objects.get(slug=slug)
    collections = theme.theme_collections.all()
    response_message = 'Все коллекции по тематике {}:'.format(theme.title)
    if not collections:
        response_message = 'В данной тематике еще нет размещенных коллекций :('
    return render(request, 'core/themes/collections_by_theme.html', {'collections': collections,
                                                                     'response_message': response_message})


def page_not_found(request, exception):
    template = 'core/404.html'
    status = 404
    context = locals()
    return render(request, template, context)


def page_not_found_500(request):
    template = 'core/500.html'
    status = 500
    context = locals()
    return render(request, template, context)
