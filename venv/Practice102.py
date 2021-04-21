"""
    Unsupervised Learning - data with no labels

    k-means Clustering - k is number of classes we except to create the model

"""
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans

iris_data = load_iris()

FEATURES = iris_data.data

clusters = 3 # k value

model = KMeans(n_clusters=clusters)

model.fit(FEATURES)

predicted_results = model.predict(FEATURES)
print(predicted_results)

unknown_value = [5.1, 3.5, 1.4, 0.2]

result = model.predict([unknown_value])
print(result)

