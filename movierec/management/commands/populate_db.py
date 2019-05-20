from django.core.management.base import BaseCommand
from movierec.models import User, Movie, Genre, Rating

import os 
import pandas as pd


class Command(BaseCommand):
	args = ''
	help = 'Author: Bernhard Jahrer. Self writen manage command to populate the database'

	_data_path = os.path.join(os.getcwd(),'movierec', 'dataset', 'ml-1m')

	def _store_movie_data(self):
		movies_file = pd.read_csv(os.path.join(self._data_path, 'movies.dat'), delimiter='::', 
			header=None, names=['movie_id', 'title', 'genre'], engine='python')

		for index, row in movies_file.iterrows():
			movie_id = row['movie_id']
			movie_title = row['title']
			genres = row['genre'].split('|')

			movie = Movie(movie_id=movie_id, title=movie_title)
			movie.save()

			for genre in genres:
				new_genre = Genre(genre=genre, movie_id=movie)
				new_genre.save()

	def _store_user_data(self):
		user_file = pd.read_csv(os.path.join(self._data_path, 'users.dat'), delimiter='::',
			header=None, names=['user_id', 'gender', 'age', 'occupation', 'zip_code'], engine='python')

		for index, row in user_file.iterrows():
			user_id = row['user_id']
			gender = row['gender']
			age = row['age']
			occupation = row['occupation']
			zip_code = row['zip_code']

			user = User(user_id=user_id, gender=gender, age=age, occupation=occupation, zip_code=zip_code)
			user.save()

	def _store_ratings_data(self):
		rating_file = pd.read_csv(os.path.join(self._data_path, 'ratings.dat'), delimiter='::',
			header=None, names=['user_id', 'movie_id', 'rating'], engine='python')

		for index, row in rating_file.iterrows():
			user = User.objects.filter(user_id=row['user_id']).order_by('user_id').first()
			movie = Movie.objects.get(movie_id=row['movie_id'])
			rating = row['rating']
			
			rating = Rating(user_id=user, movie_id=movie, rating=rating)
			rating.save()



	

	def _delete_movie_data(self):
		Movie.objects.all().delete()

	def handle(self, *arg, **kargs):
		#self._delete_movie_data()
		#self._store_movie_data()
		#self._store_user_data()
		self._store_ratings_data()