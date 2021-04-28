"""
    Feature Extraction
    API -> Dictonary Vectorizer -> Converts the dictonary into vectors
"""
from sklearn.feature_extraction import DictVectorizer
weather = [
    {'city': 'Delhi', 'temperature': 33.0},
    {'city': 'Mumbai', 'temperature': 40.0},
    {'city': 'Ludhiana', 'temperature': 23.0},
    {'city': 'Kapurthala', 'temperature': 17.0}
]
print(weather)

vectorizer = DictVectorizer()
array = vectorizer.fit_transform(weather).toarray()

print(array)

features_names = vectorizer.get_feature_names()
print(features_names)