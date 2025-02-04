import os
import pandas as pd
from django.shortcuts import render
from django.views import generic
from django.template import loader
from .models import User, Movie, Genre, Rating
from . import poster_recommender, movies, simple_recommender, nn_recommender, vote_recommender, ibcf_recommender, apriori_recommender

def get_movielist_from_rec(recommender, user_movie_id):
	similar = recommender.recommend(user_movie_id,k=10)
	similar_rows = pd.DataFrame()
	for movie_id in similar:
		similar_rows = similar_rows.append(movies[movies['id'] == movie_id])

	movieList = []
	for i in range(len(similar)):
		movieList.append([similar_rows['title'].iloc[i], "beschreibung", similar[i], similar_rows['poster_path'].iloc[i]])
	return movieList

# Create your views here.
def index(request):
	"""landing page"""
	template = loader.get_template('movierec/index.html')

	user_movie_title = request.GET.get('movie_title','')
	# find movieId of movie with title user_movie_title
	user_movie = movies[movies['title']==user_movie_title]
	# looking up for title might return multiple result or no result
	if isinstance(user_movie, pd.DataFrame):
		if user_movie.empty:
			context = {
				'recommendation_dict': {},
				'movie_title': user_movie_title,
				'poster_path': 'static/movierec/images/dino.png'
			}
			return render(request, 'movierec/index.html', context)
		else:
			user_movie = user_movie.iloc[0]
			user_movie_id = user_movie['id']

	print('User Movie ID:', user_movie_id)
	user_movie_poster = 'http://image.tmdb.org/t/p/w342{}'.format(user_movie['poster_path'])

	poster_movielist = get_movielist_from_rec(poster_recommender, user_movie_id)
	sr_movielist = get_movielist_from_rec(simple_recommender, user_movie_id)
	nn_movielist = get_movielist_from_rec(nn_recommender, user_movie_id)
	apriori_movielist = get_movielist_from_rec(apriori_recommender, user_movie_id)
	ibcf_movielist = get_movielist_from_rec(ibcf_recommender, user_movie_id)
	vote_movielist = get_movielist_from_rec(vote_recommender, user_movie_id)


	print(vote_movielist)
	recommended_list_1 = tuple(poster_movielist)
	recommended_list_2 = tuple(nn_movielist)
	recommended_list_3 = tuple(apriori_movielist)
	recommended_list_4 = tuple(sr_movielist)
	recommended_list_5 = tuple(ibcf_movielist)
	recommended_list_6 = tuple(vote_movielist)

	recommendation_lists = [recommended_list_1, recommended_list_2, recommended_list_3, 
		recommended_list_4,recommended_list_5, recommended_list_6]
	recommender_names = ['Poster Similarity Recommender', 'Nearest Neighbour Recommender', 'Apriori Recommender', 
		'One Factor IMDB Rating Recommender', 'Item Based Collaborative Filtering Recommender', 'Ensemble Vote Recommender']
	recommendation_dict = {}
	for idx, rec in enumerate(recommendation_lists):
		if rec:
			print(rec)
			recommendation_dict[recommender_names[idx]] = rec

	context = {
		'recommendation_dict': recommendation_dict,
		'movie_title': user_movie_title,
		'poster_path': user_movie_poster
	}
	return render(request, 'movierec/index.html', context)