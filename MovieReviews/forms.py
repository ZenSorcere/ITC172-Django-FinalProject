from django import forms
from .models import Movie, MovieType, Theater, Review

class MovieForm(forms.ModelForm):
    class Meta:
        model=Movie
        fields='__all__'

class TheaterForm(forms.ModelForm):
    class Meta:
        model=Theater
        fields='__all__'

class MovieTypeForm(forms.ModelForm):
    class Meta:
        model=MovieType
        fields='__all__'

class ReviewForm(forms.ModelForm):
    class Meta:
        model=Review
        fields='__all__'
    


