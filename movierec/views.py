import os
from django.shortcuts import render
from django.views import generic
from django.template import loader
from .models import User, Movie, Genre, Rating
from . import poster_recommender, movies

# Create your views here.
def index(request):
	"""landing page"""
	template = loader.get_template('movierec/index.html')

	user_movie_title = request.GET.get('movie_title','Toy Story')
	# find movieId of movie with title user_movie_title
	user_movie = movies[movies['title']==user_movie_title]
	user_movie_id = 862
	if user_movie.size != 0:
		user_movie_id = user_movie['id']

	similar = poster_recommender.recommend(float(user_movie_id),10)
	similar_rows = movies.loc[movies['id'].isin(similar)]
	similar_poster_paths = similar_rows['poster_path']

	movieList = []
	for i in range(similar.size):
		movieList.append([similar_rows['title'].iloc[i], "beschreibung", similar[i], similar_poster_paths.iloc[i]])

	recommended_list_1 = tuple(movieList)
	recommended_list_2 = tuple(movieList)
	recommended_list_3 = tuple(movieList)
	recommended_list_4 = tuple(movieList)
	recommended_list_5 = tuple(movieList)

	recommendation_lists = [recommended_list_1, recommended_list_2, recommended_list_3, recommended_list_4, recommended_list_5]

	context = {
		'recommendation_lists': recommendation_lists,
		'movie_title': user_movie_title
	}
	return render(request, 'movierec/index.html', context)
