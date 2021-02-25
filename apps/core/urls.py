from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [

    path('', views.index, name='index'),
    path('models_list/', views.models_list, name='models_list'),
    path('models_list/model_profile/<str:slug>', views.model_profile, name='model_profile')
]