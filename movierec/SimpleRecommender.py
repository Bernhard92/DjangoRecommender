import numpy as np
import pandas as pd
pd.options.mode.chained_assignment = None

class SimpleRecommender():
    recommendation = []
    popularity_levels =  [5000, 2500, 1000, 100, 10]
    recommendation_categories = ['director', 'star_1', 'star_2', 'producer', 'star_3', 'writer']

    def __init__(self, data):
        self.data = data

    def recommend_by(self, category, movie_id):

        target = self.data[self.data['id'] == movie_id][category].values[0]
        target_movies = self.data[self.data[category] == target]

        for level in self.popularity_levels:

            if len(target_movies[target_movies['vote_count'] > level]) >= 2:
                temp = target_movies[target_movies['vote_count'] > level]
                temp.sort_values('vote_average', ascending=False, inplace=True)

                if temp.iloc[0]['id'] == movie_id:
                    if temp.iloc[1]['id'] not in self.recommendation:
                        return temp.iloc[1]['id']
                else:
                    if temp.iloc[0]['id'] not in self.recommendation:
                        return temp.iloc[0]['id']
        return []



    def recommend(self, movie_id, k=10):
        self.recommendation = []
        k = k + 1
        for category in self.recommendation_categories:
            rec = self.recommend_by(category, movie_id)
            if rec:
                self.recommendation.append(rec)

        return self.recommendation
