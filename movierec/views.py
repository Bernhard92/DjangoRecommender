from django.shortcuts import render
from django.views import generic
from django.template import loader

from .models import User, Movie, Genre, Rating

# Create your views here.
def index(request):
	"""landing page"""
	template = loader.get_template('movierec/index.html')

	movieList = [["m1", "beschreibung1", 2001], ["m2", "beschreibung2", 2011], ["m3", "beschreibung3", 2005], ["m4", "beschreibung2", 2011], ["m5", "beschreibung3", 2005]]

	recommended_list_1 = tuple(movieList)
	recommended_list_2 = tuple(movieList)
	recommended_list_3 = tuple(movieList)
	recommended_list_4 = tuple(movieList)
	recommended_list_5 = tuple(movieList)

	
	recommendation_lists = [recommended_list_1, recommended_list_2, recommended_list_3, recommended_list_4, recommended_list_5]
	context = {'recommendation_lists': recommendation_lists}
 
	return render(request, 'movierec/index.html', context)


	


	