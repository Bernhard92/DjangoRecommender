#!/usr/bin/env python
# coding: utf-8

import os
import pandas as pd

class AprioriRecommender():

    def __init__(self, data, distances):
        self.distances = distances
        self.distances.columns = self.distances.columns.map(int)
        self.movies = data
        # Loading the distance matrix
        #data_path = os.path.join(os.getcwd(), 'data')
        #distances = pd.read_csv(os.path.join(data_path, 'support_small_multiprocess_vectorized.csv'),  low_memory=False, index_col=0)
        #distances.columns = distances.columns.map(int)
        #movies = pd.read_csv(os.path.join(data_path, 'movies_preprocessed.csv'))


    def recommend(self, movie_id, k=100):
        result = []
        if movie_id in self.distances.index:
            neighbors = self.distances.loc[movie_id].sort_values(ascending=False).index[1:]
            for neighbor in neighbors:
                if neighbor in self.movies['id'].values:
                    result.append(neighbor)
        else:
            print('No data for given id')
        print(result[:k])
        return result[:k]


    # Find highest support pairs


    #Forest Gump
    # movie_id = 1726
    # print('Highest Support:            ', list(distances.loc[movie_id].sort_values(ascending=False).index[1:10]))
    # result = recommend(movie_id, distances)
    # print('Highes existing in dataset: ', result, '\n')
    #
    # for movie in result[:10]:
    #     print(movies[movies['id']== movie]['title'])
