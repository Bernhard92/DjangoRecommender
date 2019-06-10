#!/usr/bin/env python
# coding: utf-8

import os
import pandas as pd

class VoteRecommender():

    def __init__(self, recommenders):
        self.recommenders = recommenders


    def recommend(self, movie_id, k=10):
        results = []
        for rec in self.recommenders:
            temp = rec.recommend(movie_id)
            print('Recommender:', rec, 'Amount of Recommendations:', len(temp))
            results += temp
        results = pd.Series(results)
        count = results.value_counts()
        print('Count:', count[:20])
        print(len(results))
        print('Movie Ids: ', count.index[:10])
        return list(count.index[:10])
