"""
Decision Tree Classifier
sklearn api - Iris Flower dataset
"""

from sklearn.datasets import load_iris
from sklearn import tree

iris_dataset = load_iris()
#print(iris_dataset)

print("Features:")
features = iris_dataset.data
print(features)

print("Labels:")
labels = iris_dataset.target
print(labels)

print("Labels with name:")
names = iris_dataset.target_names
print(names)

model = tree.DecisionTreeClassifier()

model.fit(features, labels)

known_iris1 = [5.1, 3.5, 1.4, 0.2]
known_iris2 = [7.4, 2.8, 6.1, 1.9]

predicted_labels = model.predict([known_iris1, known_iris2])
print(predicted_labels)
