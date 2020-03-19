from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import MovieType, Movie, Review, Theater
from .forms import MovieTypeForm, MovieForm, ReviewForm, TheaterForm
from django.contrib.auth.decorators import login_required


def index (request):
    return render(request, 'MovieReviews/index.html')

def getgenres(request):
    genre_list=MovieType.objects.all()
    return render(request, 'MovieReviews/genres.html' ,{'genre_list' : genre_list})

def getmovies(request):
    movie_list=Movie.objects.all()
    return render(request, 'MovieReviews/movies.html' , {'movie_list' : movie_list})

def moviedetails(request, id):
    movie=get_object_or_404(Movie, pk=id)
    theater=get_object_or_404(Theater, pk=id)
    #theater=Theater.objects.filter(theater=id)
    reviews=get_object_or_404(Review, pk=id)
    #reviews=Review.objects.filter(movie=id)
    context={
        'movie' : movie,
        'theater' : theater,
        'reviews' : reviews,
    }
    return render(request, 'MovieReviews/moviedetails.html', context=context)

def gettheaters(request):
    theater_list=Theater.objects.all()
    return render(request, 'MovieReviews/theaters.html' , {'theater_list' : theater_list})

@login_required
def newMovie(request):
     form=MovieForm
     if request.method=='POST':
          form=MovieForm(request.POST)
          if form.is_valid():
               post=form.save(commit=True)
               post.save()
               form=MovieForm()
     else:
          form=MovieForm()
     return render(request, 'MovieReviews/newmovie.html', {'form': form})

@login_required
def newTheater(request):
     form=TheaterForm
     if request.method=='POST':
          form=TheaterForm(request.POST)
          if form.is_valid():
               post=form.save(commit=True)
               post.save()
               form=TheaterForm()
     else:
          form=TheaterForm()
     return render(request, 'MovieReviews/newtheater.html', {'form': form})
                            
@login_required
def newMovieType(request):
     form=MovieTypeForm
     if request.method=='POST':
          form=MovieTypeForm(request.POST)
          if form.is_valid():
               post=form.save(commit=True)
               post.save()
               form=MovieTypeForm()
     else:
          form=MovieTypeForm()
     return render(request, 'MovieReviews/newgenre.html', {'form': form})

@login_required
def newReview(request):
     form=ReviewForm
     if request.method=='POST':
          form=ReviewForm(request.POST)
          if form.is_valid():
               post=form.save(commit=True)
               post.save()
               form=ReviewForm()
     else:
          form=ReviewForm()
     return render(request, 'MovieReviews/newreview.html', {'form': form})


def loginmessage(request):
    return render(request, 'MovieReviews/loginmessage.html')

def logoutmessage(request):
    return render(request, 'MovieReviews/logoutmessage.html')