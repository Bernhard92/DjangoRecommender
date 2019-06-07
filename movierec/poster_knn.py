from builtins import range
from builtins import object
import numpy as np
from past.builtins import xrange


class PosterKNN(object):
    """ a kNN recommender with L2 distance """

    def __init__(self):
        pass

    def train(self, X, y):
        """
        Train the classifier. For k-nearest neighbors this is just
        memorizing the training data.

        Inputs:
        - X: A numpy array of shape (num_train, D) containing the training data
          consisting of num_train samples each of dimension D.
        - y: A numpy array of shape (N,) containing the training movieIds, where
             y[i] is the movieIds for X[i].
        """
        self.X_train = X
        self.y_train = y

    def recommend(self, movieId, k=1):
        """
        Predict movieIds for test data using this classifier.

        Inputs:
        - movieId: movieId of input movie that can be found in y_train.
        - k: The number of nearest neighbors we want to find.

        Returns:
        - y: A numpy array of shape (k,) containing predicted movieIds.
        """
        movie_idx = np.where(self.y_train == movieId)
        dists = self.compute_distances(self.X_train[movie_idx])

        most_similar_idxs = np.argsort(dists)
        #don't recommend the input movie
        most_similar_idxs = np.delete(most_similar_idxs, np.where(most_similar_idxs == movie_idx[0]))

        return self.y_train[most_similar_idxs[:k]]

    def compute_distances(self, X):
        """
        Compute the distance between each test point in X and each training point
        in self.X_train using a loop over the training data.

        Inputs:
        - X: A numpy array containing input data.

        Returns:
        - dists: A numpy array of shape (num_train) where dists[j]
          is the Euclidean distance between the test point and the jth training
          point.
        """
        num_train = self.X_train.shape[0]
        dists = np.zeros(num_train)
        for j in range(num_train):
            dists[j] = np.sqrt(np.sum((self.X_train[j]-X)**2))
        return dists
