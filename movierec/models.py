from django.db import models
 
import datetime

# Create your models here.
class Movie(models.Model):
	def __str__(self):
		return self.title

	movie_id = models.IntegerField()
	title = models.CharField(max_length=300)

class Genre(models.Model):
	genre = models.CharField(max_length=100)
	movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)

class User(models.Model):
	user_id = models.IntegerField()
	gender = models.CharField(max_length=1)
	age = models.IntegerField()
	occupation = models.CharField(max_length=300)

class Rating(models.Model):
	user_id = models.ForeignKey(User, on_delete=models.CASCADE)
	movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
	rating = models.FloatField()