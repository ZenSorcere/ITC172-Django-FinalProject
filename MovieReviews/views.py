from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import MovieType, Movie, Review, Theater

def index (request):
    return render(request, 'MovieReviews/index.html')

def getgenres(request):
    genre_list=MovieType.objects.all()
    return render(request, 'moviereviews/genres.html' ,{'genre_list' : genre_list})

def getmovies(request):
    movie_list=Movie.objects.all()
    return render(request, 'moviereviews/movies.html' , {'movie_list' : movie_list})

def moviedetails(request, id):
    movie=get_object_or_404(Movie, pk=id)
    #theater=Theater.objects.filter(theater=id)
    reviews=get_object_or_404(Review, pk=id)
    #reviews=Review.objects.filter(movie=id)
    context={
        'movie' : movie,
        #'theater' : theater,
        'reviews' : reviews,
    }
    return render(request, 'moviereviews/moviedetails.html', context=context)



