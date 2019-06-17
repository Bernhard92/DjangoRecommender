import os
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.neighbors import NearestNeighbors
from scipy.sparse import csr_matrix
import gc





class ItemBasedCollaborativeFiltering():
    def __init__(self, ratings, movies, k=10):
        self.threshold_movie='10' 
        self.threshold_user='300'

        #filter unpopular movies and opinions
        df_movies_cnt = pd.DataFrame(ratings.groupby('movieId').size(), columns=['count'])
        popular_movies = list(set(df_movies_cnt.query('count >= '+self.threshold_movie).index))
        movies_filter = ratings.movieId.isin(popular_movies).values

        df_users_cnt = pd.DataFrame(ratings.groupby('userId').size(), columns=['count'])
        active_users = list(set(df_users_cnt.query('count >= '+self.threshold_user).index)) 
        users_filter = ratings.userId.isin(active_users).values

        ratings_filtered = ratings[movies_filter & users_filter]

        #create pivot-table
        self.movie_features = ratings_filtered.pivot(index='movieId', columns='userId', values='rating').fillna(0)

        # convert dataframe of movie features to scipy sparse matrix
        movie_features_compressed = csr_matrix(self.movie_features.values)


        self.data = movie_features_compressed
        self.movies = movies
        self.model_knn = NearestNeighbors(metric='cosine', algorithm='brute', n_neighbors=k, n_jobs=-1)
        self.model_knn.fit(self.data)

        # clean up
        del df_movies_cnt, df_users_cnt
        del ratings, ratings_filtered, #movie_features
        gc.collect()

    def recommend(self, movie_id, k=10):
        result = []
        if movie_id in self.movie_features.index:
            distances, recommendations = self.model_knn.kneighbors(self.data[movie_id])
            neighbors = recommendations[0][1:]
            
            for neighbor in neighbors:
                if neighbor in self.movies['id'].values:
                    result.append(neighbor)
        else:
            print('no result for given Id')
        return result[:k]

