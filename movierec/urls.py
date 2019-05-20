from django.urls import path

from . import views

app_name = 'movierec'
urlpatterns = [
	# ex: /movierec/
	#path('', views.IndexView.as_view(), name='index'),
	path('', views.index, name='index'),	

	# ex: /movierec/5/
	#path('<int:pk>/', views.DetailView.as_view(), name='detail'),

	# ex: /movierec/5/results/
	#path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),

	# ex: /movierec/5/vote/
	#path('<int:question_id>/vote/', views.vote, name='vote'),
	
]