from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('getgenres/', views.getgenres, name= 'genres'),
    path('getmovies/', views.getmovies, name= 'movies'),
    path('moviedetails/<int:id>', views.moviedetails, name='moviedetails'),
]