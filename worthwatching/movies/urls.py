from django.urls import path
from . import views

urlpatterns = [
    path('', views.movies, name='movies'),
    path('add-movie/', views.addMovie, name='add-movie'),
]
