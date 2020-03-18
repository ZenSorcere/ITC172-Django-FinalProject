from django.db import models
from django.contrib.auth.models import User

class MovieType(models.Model):
    genrename=models.CharField(max_length=255)
    genredesc=models.TextField(null=True, blank=True)

    def __str_(self):
        return self.genrename

    class Meta:
        db_table='movietype'
        verbose_name_plural='movietypes'

class Theater(models.Model):
    theatername=models.CharField(max_length=255)
    theaterurl=models.URLField(null=True, blank=True)
    theaterscreens=models.SmallIntegerField(null=True, blank=True)
    theateraddress=models.TextField(max_length=255, null=True, blank=True)
    theatercity=models.CharField(max_length=64)
    theaterstate=models.CharField(max_length=2)
    theaterzip=models.CharField(max_length=5)
    user=models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.theatername
    
    class Meta:
        db_table='theater'
        verbose_name_plural='theaters'

class Review(models.Model):
    revtitle=models.CharField(max_length=255)
    revdate=models.DateField()
    movietitle=models.ForeignKey("Movie", on_delete=models.DO_NOTHING)
    theatertitle=models.ForeignKey(Theater, on_delete=models.DO_NOTHING)
    user=models.ForeignKey(User, on_delete=models.DO_NOTHING)
    RATINGS = (
        ('0', '0 Stars'),
        ('.5', '1/2 Star'),
        ('1', '1 Star'),
        ('1.5', '1.5 Stars'),
        ('2', '2 Stars'),
        ('2.5', '2.5 Stars'),
        ('3', '3 Stars'),
        ('3.5', '3.5 Stars'),
        ('4', '4 Stars'),
        ('4.5', '4.5 Stars'),
        ('5', '5 Stars'),
    )
    rating=models.CharField(max_length=4, choices=RATINGS, null=True, blank=True)
    revdesc=models.TextField()

    def __str__(self):
        return self.revtitle

    class Meta:
        db_table='review'
        verbose_name_plural='reviews'

class Movie(models.Model):
    moviename=models.CharField(max_length=255)
    movietype=models.ForeignKey(MovieType, on_delete=models.DO_NOTHING)
    theater=models.ForeignKey(Theater, on_delete=models.DO_NOTHING)
    user=models.ForeignKey(User, on_delete=models.DO_NOTHING)
    rating=models.ForeignKey(Review, on_delete=models.DO_NOTHING, null=True, blank=True)
    moviedesc=models.TextField(null=True, blank=True)

    def __str__(self):
        return self.moviename

    class Meta:
        db_table='movie'
        verbose_name_plural='movies'









