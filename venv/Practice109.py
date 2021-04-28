"""
    Feature Extraction / Dimensionlity Reduction

"""
from sklearn.feature_selection import VarianceThreshold

X = [
    [0,2,2,3],
    [0,1,4,3],
    [0,1,1,3],
]

selector = VarianceThreshold()
X = selector.fit_transform(X)
