from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.core.files.base import ContentFile
from django.shortcuts import redirect, render
from django.urls.base import reverse
from django.views.decorators.http import require_POST
from django.http import HttpResponse
import json

from .forms import ImageUploadForm
from .models import Image, Models, CosplayPost
from config.settings import ALLOWED_HOSTS


def like(request):
    if request.method == 'POST':
        user = request.user
        pk = request.POST.get('pk', None)
        image = Image.objects.get(pk=pk)

        if image.likes.filter(id=user.id).exists():
            # user has already liked this image
            # remove like/user
            image.likes.remove(user)
        else:
            # add a new like for a image
            image.likes.add(user)

    context = {'likes_count': image.total_likes}

    return HttpResponse(json.dumps(context), content_type='application/json')


def stars(request):
    """ функция для подсчета звед у моделей"""
    if request.method == 'POST':
        user = request.user
        slug = request.POST.get('slug', None)
        model = Models.objects.get(slug=slug)

        if model.stars.filter(id=user.id).exists():
            model.stars.remove(user)
        else:
            model.stars.add(user)

    context = {'stars_count': model.total_stars}

    return HttpResponse(json.dumps(context), content_type='application/json')


@staff_member_required
def admin_upload_image(request, pk):
    """ Форма загрузки нескольких изображений на сайт"""
    post = CosplayPost.objects.get(id=pk)
    if request.method == 'POST':
        # перебираем все файлы, загруженные из формы
        for file in request.FILES.getlist('images'):
            # первому файлу ставим признак for_title
            if file == request.FILES.getlist('images')[0]:
                instance = Image(post=post, image=file, for_title=True)
            else:
                instance = Image(post=post, image=file)
            instance.save()

        messages.success(request, 'Изображения успешно загружены')
        return redirect('admin:index')

    context = locals()
    return render(request, 'core/admin/post/upload_image.html', context)
