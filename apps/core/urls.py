from django.urls import path
from . import views
from . import services

app_name = 'core'

urlpatterns = [

    path('', views.IndexView.as_view(), name='index'),
    path('models_list/', views.ModelListView.as_view(), name='models_list'),
    path('models_list/model_profile/<slug:slug>', views.ModelDetailView.as_view(), name='model_profile'),
    path('stars/', services.stars, name='stars'),
    path('image_view/<int:pk>/', views.ImageDetailView.as_view(), name='image_view'),
    path('image/like/', services.like, name='like'),
    path('rubrics_list', views.RubricList.as_view(), name='rubrics_list'),
    path('posts_by_rubric/<slug:slug>/', views.RubricDetailView.as_view(), name='posts_by_rubric'),
    path('top_posts_list/', views.TopPostsListView.as_view(), name='top_posts_list'),
    path('posts/<slug:slug>/', views.PostDetailView.as_view(), name='post_view'),
    path('search/', views.search, name='search'),
    path('admin_upload_images/<int:pk>', services.admin_upload_image, name='admin_upload_images'),
]