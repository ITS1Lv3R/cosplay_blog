from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler400, handler403, handler404, handler500

from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('apps.account.urls')),
    path('', include('apps.core.urls', namespace='core')),
    path('', include('social_django.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

handler400 = 'apps.core.views.page_not_found'
handler403 = 'apps.core.views.page_not_found'
handler404 = 'apps.core.views.page_not_found'
handler500 = 'apps.core.views.page_not_found_500'
