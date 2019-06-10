import numpy as np
import pandas as pd
from sklearn import preprocessing
pd.options.mode.chained_assignment = None
from sklearn.neighbors import NearestNeighbors

class NNRecommender():
    features = ['id', 'popularity', 'runtime', 'vote_average', 'vote_count', 'Action',
       'Adventure', 'Animation', 'Comedy', 'Crime', 'Documentary', 'Drama',
       'Family', 'Fantasy', 'Foreign', 'History', 'Horror', 'Music', 'Mystery',
       'Romance', 'Science Fiction', 'TV Movie', 'Thriller', 'War', 'Western',
       'en', 'fr', 'it', 'ja', 'de', 'es', 'ru', 'woman director',
       'independent film', 'murder', 'based on novel', 'musical', 'sex',
       'violence', 'nudity', 'biography', 'revenge', 'suspense', 'love',
       'female nudity', 'sport', 'police', 'teenager', 'duringcreditsstinger',
       'sequel', 'friendship', 'world war ii']

    def __init__(self, data, k=10, metric='minkowski', leaf_size=30):
        # normalize data
        data['popularity'] = data['popularity'] / data['popularity'].max()
        data['runtime'] = data['runtime'] / data['runtime'].max()
        data['vote_average'] = data['vote_average'] / data['vote_average'].max()
        data['vote_count'] = data['vote_count'] / data['vote_count'].max()
        # impute missing data
        data['runtime'] = data['runtime'].fillna(data['runtime'].mean())
        self.data = data[self.features]
        self.nn = NearestNeighbors(n_neighbors=k, metric=metric, leaf_size=leaf_size)
        self.nn.fit(self.data.drop('id', axis=1))

    def _indices_to_movie_id(self, indices):
        movie_ids = []
        for index in indices:
            movie_ids.append(self.data.iloc[index]['id'].values)
        return movie_ids[0][1:]

    def recommend(self, movie_id, k=10, return_distance=False):
        movie = self.data[self.data['id'] == movie_id].drop('id', axis=1).values
        distances, indices = self.nn.kneighbors(movie)
        recommendations = self._indices_to_movie_id(indices)
        if return_distance:
            return recommendations, distances
        return list(recommendations)
