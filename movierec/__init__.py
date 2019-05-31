# initialize poster recommender at startup
import numpy as np
import os
import pandas as pd
from skimage.transform import resize
from skimage import io
from movierec.poster_knn import PosterKNN

print('starting to load poster data for recommender')
image_data_feats = np.load(os.path.join(os.getcwd(),'movierec/data/image_features_X.npy'))
image_data_y = np.load(os.path.join(os.getcwd(),'movierec/data/image_ids_y.npy'))

print('initialize poster recommender')
poster_recommender = PosterKNN()
poster_recommender.train(image_data_feats,image_data_y)

print('initialize movie table')
data_path = os.path.join(os.getcwd(), 'movierec/data/the-movies-dataset/')
movies = pd.read_csv(os.path.join(data_path, 'movies_preprocessed.csv'))
