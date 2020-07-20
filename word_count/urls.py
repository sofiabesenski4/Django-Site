from django.urls import path

from . import views


app_name ='word_count'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:target_id>/details', views.details, name='details'),
    path('search/',views.search, name='search')
]