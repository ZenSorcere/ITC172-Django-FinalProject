from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('getgenres/', views.getgenres, name= 'genres'),
    path('newgenre/', views.newMovieType, name='newgenre'),
    path('getmovies/', views.getmovies, name= 'movies'),
    path('moviedetails/<int:id>', views.moviedetails, name='moviedetails'),
    path('gettheaters/', views.gettheaters, name= 'theaters'),
    path('newmovie/', views.newMovie, name='newmovie'),
    path('newtheater/', views.newTheater, name='newtheater'),
    path('newreview/', views.newReview, name='newreview'),
    path('loginmessage/', views.loginmessage, name='loginmessage'),
    path('logoutmessage/', views.logoutmessage, name='logoutmessage'),
]