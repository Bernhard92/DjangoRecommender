
import os 
import numpy as np
import pandas as pd
from models import User, Movie, Genre, Rating

data_path = os.path.join(os.getcwd(),'movierec', 'dataset', 'ml-1m')

movies_file = pd.read_csv(os.path.join(data_path, 'movies.dat'), delimiter='::', 
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





	

