from django.urls import path
from . import views


app_name = 'core'

urlpatterns = [

    path('', views.IndexView.as_view(), name='index'),
    path('models_list/', views.ModelListView.as_view(), name='models_list'),
    path('models_list/model_profile/<slug:slug>', views.model_profile, name='model_profile'),
    path('image_view/<slug:slug>/', views.image_view, name='image_view'),
    path('rubrics_list', views.RubricView.as_view(), name='rubrics_list'),
    path('collections_by_rubric/<slug:slug>/', views.collections_by_rubric, name='collections_by_rubric')

]