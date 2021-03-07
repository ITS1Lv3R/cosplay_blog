from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.http import HttpResponse
import json
from .models import Image, Models


@login_required
@require_POST
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


@login_required
@require_POST
def stars(request):
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
