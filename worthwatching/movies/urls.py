from django.urls import path
from . import views

urlpatterns = [
    path('', views.movies, name='movies'),
    path('add-movie/', views.addMovie, name='add-movie'),
    path('update-movie/<str:pk>/', views.updateMovie, name='update-movie'),
    path('delete-movie/<str:pk>/', views.deleteMovie, name='delete-movie'),

]
