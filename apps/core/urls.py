from django.urls import path
from . import views
from . import services

app_name = 'core'

urlpatterns = [

    path('', views.IndexView.as_view(), name='index'),
    path('models_list/', views.ModelListView.as_view(), name='models_list'),
    path('models_list/model_profile/<slug:slug>', views.model_profile, name='model_profile'),
    path('stars/', services.stars, name='stars'),
    path('image_view/<slug:slug>/', views.image_view, name='image_view'),
    path('image/like/', services.like, name='like'),
    path('rubrics_list', views.RubricView.as_view(), name='rubrics_list'),
    path('collections_by_rubric/<slug:slug>/', views.collections_by_rubric, name='collections_by_rubric'),
    path('collection_list/', views.CollectionView.as_view(), name='collection_list'),
    path('search/', views.search, name='search')

]