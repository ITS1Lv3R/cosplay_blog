from django.contrib import messages
from django.shortcuts import render
from django.views.generic.base import View
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from apps.core.models import Models, CosplayPost, Image, CosplayRubric
from django.db.models import Q


class IndexView(ListView):
    """ Вью для главной страницы, все посты"""
    queryset = CosplayPost.objects.all()
    template_name = 'core/index.html'
    context_object_name = 'posts'
    paginate_by = 6


class PostDetailView(DetailView):
    """ Детальная вью для изображений"""
    model = CosplayPost
    template_name = 'core/post/post_view.html'
    context_object_name = 'post'


class TopPostsListView(ListView):
    """ Список первых 10 постов"""
    queryset = CosplayPost.objects.filter()[:10]
    template_name = 'core/post/top_posts_list.html'
    context_object_name = 'posts'
    paginate_by = 6


class ModelListView(ListView):
    """ Список моделей """
    queryset = Models.objects.all().order_by('name')
    template_name = 'core/models/models_list.html'
    context_object_name = 'models'
    paginate_by = 6


class ModelDetailView(DetailView):
    """ Список моделей """
    model = Models
    template_name = 'core/models/model_profile.html'
    context_object_name = 'model'


class ImageDetailView(DetailView):
    """ Детальная вью для изображений"""
    model = Image
    template_name = 'core/image_view.html'
    context_object_name = 'image'


class RubricList(ListView):
    """ Список всех тематик"""
    queryset = CosplayRubric.objects.all().order_by('title')
    template_name = 'core/rubric/rubric_list.html'
    context_object_name = 'rubrics'
    paginate_by = 6


class RubricDetailView(DetailView):
    """ отображает посты по выбранной рубрике"""
    model = CosplayRubric
    template_name = 'core/rubric/posts_by_rubric.html'
    context_object_name = 'rubric'


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


def search(request):
    """ функция поиска постов"""
    query = request.GET.get('q')
    # изменяем регистр первого символа запроса. проанализировать надо будет
    query = query.title()
    posts = CosplayPost.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))
    return render(request, 'core/search.html', {'posts': posts,
                                                'query': query})

