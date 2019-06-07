import os
import pandas as pd
import numpy as np
import re
import urllib.request


# poster size can be requested by w*
# possible sizes: "w92", "w154", "w185", "w342", "w500", "w780", or "original"
poster_path_url = 'http://image.tmdb.org/t/p/w92'

def extract_posters(movies, to_folder):
    '''
    Takes the preprocessed movie features and downloads the images of all movies where a poster path is provided.
    
    Inputs: 
    movies: movie data - Pandas dataframe
    to_folder: Path to the output folder where images get downloaded
    
    Output:
    skipped_posters: List of movieIds from all movies that don't contain a poster path
    '''
    skipped_posters = []
    for idx, movie in movies.iterrows(): 
        poster_path = movie['poster_path']
        if poster_path is not None:
            # download file from url and save it to_folder with movieId as name
            image_name = str(movie['id'])+'.jpg'
            exists = os.path.isfile(to_folder+image_name)
            if not exists:
                try:
                    urllib.request.urlretrieve(poster_path_url+poster_path, to_folder+image_name)
                except Exception as e:
                    print('http exception - skipping poster of movieId: {}'.format(movie['id']))
                    skipped_posters.append(movie['id'])
                    pass
        else:
            print('skipping poster of movieId: {}'.format(movie['id']))
            skipped_posters.append(movie['id'])
    return skipped_posters
            
    