from django.shortcuts import render

from apps.core.models import Models


def index(request):
    """ Главная страница"""
    return render(request, 'core/index.html')


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
        message = 'У данной модели нет коллекций'
    context = locals()
    return render(request, 'core/models/model_profile.html', context)


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
