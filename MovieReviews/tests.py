from django.test import TestCase
from .views import index, getgenres, getmovies, gettheaters, moviedetails
from django.urls import reverse
from django.contrib.auth.models import User
from .models import MovieType, Movie, Review, Theater
from .forms import MovieTypeForm, MovieForm, ReviewForm, TheaterForm

# MODEL TESTS

class MovieTypeTest(TestCase):
    def test_string(self):
        cat=MovieType(genrename="Murder")
        self.assertEqual(str(cat), cat.genrename)
# this the MovieTpye object issue makes this test fail!

    def test_table(self):
        self.assertEqual(str(MovieType._meta.db_table), 'movietype')

class MovieTest(TestCase):
    def setup(self):
        genre = MovieType(genrename='comedy')
        theater = Theater(theatername='odeon')
        user = User(username='testuser1')
        movie=Movie(moviename='Scrooged', movietype=genre, theater=theater, user=user)
    
    def test_string(self):
        #mov = self.setup()
        mov = Movie(moviename='Scrooged')
        self.assertEqual(str(mov), mov.moviename)

    def test_table(self):
        self.assertEqual(str(Movie._meta.db_table), 'movie')

class TheaterTest(TestCase):
    def setup(self):
        theater=Theater(theatername='Cinema', theateraddress='123 NE 123 St', theatercity='Seattle', theaterstate='WA', theaterzip='98101')

    def test_string(self):
        #the = self.setup()
        the=Theater(theatername='odeon2')
        self.assertEqual(str(the), the.theatername)

    def test_table(self):
        self.assertEqual(str(Theater._meta.db_table), 'theater')

class ReviewTest(TestCase):
    def test_string(self):
        rev=Review(revtitle="Best Review")
        self.assertEqual(str(rev), rev.revtitle)

    def test_table(self):
        self.assertEqual(str(Review._meta.db_table), 'review')

# VIEWS TESTS

class IndexTest(TestCase):
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

class GetGenresTest(TestCase):
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('genres'))
        self.assertEqual(response.status_code, 200)
  
class GetMoviesTest(TestCase):
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('movies'))
        self.assertEqual(response.status_code, 200)

class GetTheatersTest(TestCase):
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('theaters'))
        self.assertEqual(response.status_code, 200)

class MovieDetailsTest(TestCase):

    def setUp(self):
        self.u=User.objects.create(username='myuser')
        self.type=MovieType.objects.create(genrename='documentary')
        self.the=Theater.objects.create(theatername='Uptown', theatercity='queen anne', theaterstate='WA', theaterzip='98122', user=self.u)
        self.prod = Movie.objects.create(moviename='Apollo11', movietype=self.type, theater=self.the, user=self.u)
        self.rev1=Review.objects.create(revtitle='movreview', revdate='2019-04-03', movietitle=self.prod, theatertitle=self.the, user=self.u, rating=4, revdesc='some review')
        #self.rev1.user.add(self.u)
        

    def test_movie_detail_success(self):
        response = self.client.get(reverse('moviedetails', args=(self.prod.id,)))
        # Assert that self.post is actually returned by the post_detail view
        self.assertEqual(response.status_code, 200)
    #This may(??) be fixed when I get the reviews/movies to line up

# FORM TESTS

class Theater_Form_Test(TestCase):
    def test_typeform_is_valid(self):
        self.test_user=User.objects.create_user(username='testuser1', password='P@ssw0rd1')
        form=TheaterForm(data={'theatername': "odeon", 'theaterurl': "http://www.google.com", 'theaterscreens': "10", 'theateraddress': "123 NE 123rd St.", 'theatercity': "Seattle", 'theaterstate' : "WA", 'theaterzip' : "98125", 'user': self.test_user})
        self.assertTrue(form.is_valid())
    
    def test_typeform_minus_address(self):
        form=TheaterForm(data={'theateraddress': ""})
        self.assertFalse(form.is_valid())

    def test_typeform_empty(self):
        form=TheaterForm(data={'theatername': ""})
        self.assertFalse(form.is_valid())

class Review_Form_Test(TestCase):
    def test_typeform_is_valid(self):
        self.test_user=User.objects.create_user(username='testuser2', password='P@ssw0rd1')
        self.type=MovieType.objects.create(genrename='documentary')
        self.the=Theater.objects.create(theatername='Uptown', theatercity='queen anne', theaterstate='WA', theaterzip='98122', user=self.test_user)
        self.prod = Movie.objects.create(moviename='Apollo11', movietype=self.type, theater=self.the, user=self.test_user)
        form=ReviewForm(data={'revtitle': "great", 'revdate': "2020-03-18", 'movietitle': self.prod, 'theatertitle' : self.the, 'user': self.test_user, 'rating': "4.5", 'revdesc': "good film"})
        self.assertTrue(form.is_valid())
    
    def test_typeform_minus_rating(self):
        form=ReviewForm(data={'rating': ""})
        self.assertFalse(form.is_valid())

    def test_typeform_empty(self):
        form=ReviewForm(data={'revtitle': ""})
        self.assertFalse(form.is_valid())

class Movie_Form_Test(TestCase):
    def test_typeform_is_valid(self):
        self.test_user=User.objects.create_user(username='testuser2', password='P@ssw0rd1')
        self.type=MovieType.objects.create(genrename='documentary')
        self.the=Theater.objects.create(theatername='Uptown', theatercity='queen anne', theaterstate='WA', theaterzip='98122', user=self.test_user)
        self.prod = Movie.objects.create(moviename='Apollo11', movietype=self.type, theater=self.the, user=self.test_user)
        self.rev=Review.objects.create(revtitle='movreview', revdate='2019-04-03', movietitle=self.prod, theatertitle=self.the, user=self.test_user, rating=4, revdesc='some review')
        form=MovieForm(data={'moviename':"Apollo11", 'movietype': self.type, 'theater': self.the, 'user': self.test_user, 'moviedesc': "some review"})
        self.assertTrue(form.is_valid())
    
    def test_typeform_minus_desc(self):
        form=MovieForm(data={'moviedesc': ""})
        self.assertFalse(form.is_valid())

    def test_typeform_empty(self):
        form=MovieForm(data={'moviename': ""})
        self.assertFalse(form.is_valid())

class MovieType_Form_Test(TestCase):
    def test_typeform_is_valid(self):
        self.test_user=User.objects.create_user(username='testuser2', password='P@ssw0rd1')
        form=MovieTypeForm(data={'genrename':"western", 'genredesc': "deserts and cowboys"})
        self.assertTrue(form.is_valid())

    def test_typeform_minus_desc(self):
        form=MovieForm(data={'moviedesc': ""})
        self.assertFalse(form.is_valid())

    def test_typeform_empty(self):
        form=MovieForm(data={'genrename': ""})
        self.assertFalse(form.is_valid())
    

# AUTHENTICATION TEST (using newtheater)

class New_Theater_authentication_test(TestCase):
    def setUp(self):
        self.test_user=User.objects.create_user(username='testuser1', password='P@ssw0rd1')
        self.prod = Theater.objects.create(theatername='7 Gables', theaterurl= 'http://www.dell.com', theaterscreens='5', theateraddress='123 123rd St NE', theatercity='Walla Walla', theaterstate='WA', theaterzip="98275", user=self.test_user)

    def test_redirect_if_not_logged_in(self):
        response=self.client.get(reverse('newtheater'))
        self.assertRedirects(response, '/accounts/login/?next=/MovieReviews/newtheater/')

    def test_Logged_in_uses_correct_template(self):
        login=self.client.login(username='testuser1', password='P@ssw0rd1')
        response=self.client.get(reverse('newtheater'))
        self.assertEqual(str(response.context['user']), 'testuser1')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'MovieReviews/newtheater.html')
                                        