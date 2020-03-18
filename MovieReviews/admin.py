from django.contrib import admin
from .models import MovieType, Movie, Review, Theater

admin.site.register(MovieType)
admin.site.register(Movie)
admin.site.register(Review)
admin.site.register(Theater)
