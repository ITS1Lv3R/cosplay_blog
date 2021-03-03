from django.contrib import messages
from django.shortcuts import render
from django.views.generic.base import View
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from apps.core.forms import AddCommentForm
from apps.core.models import Models, CosplayBlogPost, Image, CosplayRubric


class IndexView(ListView):
    """ Вью для главной страницы"""
    queryset = CosplayBlogPost.objects.all()
    template_name = 'core/index.html'
    context_object_name = 'posts'


class ModelListView(ListView):
    """ Список моделей """
    queryset = Models.objects.all()
    template_name = 'core/models/models_list.html'
    context_object_name = 'models'


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


def image_view(request, slug):
    """ Детальная вью для изображений"""
    image = Image.objects.get(slug=slug)

    if request.method == 'POST':
        comment_form = AddCommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.text = comment_form.cleaned_data['text']
            new_comment.author = request.user
            new_comment.image = image
            new_comment.save()
            messages.success(request, 'Сообщение добавлено')
    else:
        comment_form = AddCommentForm()

    return render(request, 'core/image_view.html', {'comment_form': comment_form,
                                                    'image': image})


class RubricView(ListView):
    """ Список всех тематик"""
    queryset = CosplayRubric.objects.all()
    template_name = 'core/rubric/rubric_list.html'
    context_object_name = 'rubrics'


def collections_by_rubric(request, slug):
    """ Страница с коллекциями по темам"""
    rubric = CosplayRubric.objects.get(slug=slug)
    collections = rubric.collections.all()
    response_message = 'Все коллекции по тематике {}:'.format(rubric.title)
    if not collections:
        response_message = 'В данной тематике еще нет размещенных коллекций :('
    context = locals()
    return render(request, 'core/rubric/collections_by_rubric.html', context)


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
