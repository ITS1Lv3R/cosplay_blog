from django.urls import path
from . import views


app_name = 'core'

urlpatterns = [

    path('', views.index, name='index'),
    path('models_list/', views.models_list, name='models_list'),
    path('models_list/model_profile/<str:slug>', views.model_profile, name='model_profile'),
    path('image_view/<str:slug>/', views.ImageView.as_view(), name='image_view'),
    path('themes_list', views.ThemeView.as_view(), name='themes_list'),
    path('collections_by_theme/<str:slug>/', views.collections_by_theme, name='collections_by_theme')

]