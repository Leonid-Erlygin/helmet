import numpy as np
from scipy.spatial import ConvexHull


class PointsMatcherConvexHull():
    def __init__(self, D):
        """
        Keyword arguments:
        D -- a small threshold distance used to match points after some transform
        """
        self.D = D


    def find_transform(self, s1 : np.ndarray, s2 : np.ndarray) -> (np.ndarray, np.ndarray):
        """
        computes best affine transform between two sets s1, s2

        Keyword arguments:
        s1, s2 -- sets of points on 2d plane

        return:
        A, b -- 2x2 and 2x1 arrays, defining the optimal affine transform between two sets s1, s2
        """
        c1 = ConvexHull(s1)
        c2 = ConvexHull(s2)
        


def test_matcher():
    pm = PointsMatcherConvexHull(0.1)

if __name__ == '__main__':
    test_matcher()

