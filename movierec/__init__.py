import numpy as np
import os
import pandas as pd
from skimage.transform import resize
from skimage import io
from movierec.recommender.poster_knn import PosterKNN
from movierec.recommender.SimpleRecommender import SimpleRecommender
from movierec.recommender.NNRecommender import NNRecommender
from movierec.recommender.AprioriRecommender import AprioriRecommender
from movierec.recommender.VoteRecommender import VoteRecommender
from movierec.recommender.ItemBasedCF import ItemBasedCollaborativeFiltering


# initialize poster recommender
print('starting to load poster data for recommender')
image_data_feats = np.load(os.path.join(os.getcwd(),'movierec/data/image_features_X.npy'))
image_data_y = np.load(os.path.join(os.getcwd(),'movierec/data/image_ids_y.npy'))

print('initialize poster recommender')
poster_recommender = PosterKNN()
poster_recommender.train(image_data_feats,image_data_y)

# initialize movies table
print('initialize movie table')
data_path = os.path.join(os.getcwd(), 'movierec/data/the-movies-dataset/')
movies = pd.read_csv(os.path.join(data_path, 'movies_preprocessed.csv'))
movies = movies.drop_duplicates(subset='id')
ratings = pd.read_csv(os.path.join(data_path, 'ratings.csv'))

#initialize SimpleRecommender
print('initialize simple recommender')
simple_recommender = SimpleRecommender(movies.copy())

# initialize NNRecommender
print('initialize NN recommender')
nn_recommender = NNRecommender(movies.copy())
nn_recommender_vote = NNRecommender(movies.copy(), k=100)

# initialize AprioriRecommender
print('initialize distances for apriori')
distances = pd.read_csv(os.path.join(data_path, 'support_small_multiprocess_vectorized.csv'),  low_memory=False, index_col=0)
print('initialize apriori recommender')
apriori_recommender = AprioriRecommender(movies.copy(), distances)

# initialize ItemBasedCollaborativeFiltering
print('initialize item based collaborative filtering')
ibcf_recommender = ItemBasedCollaborativeFiltering(ratings, movies.copy(), k=20)

# initialize VoteRecommender
print('initialize vote recommender')
vote_recommender = VoteRecommender([poster_recommender,simple_recommender,nn_recommender_vote, apriori_recommender, ibcf_recommender]) 


