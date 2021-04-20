from sklearn.datasets import load_iris
from sklearn import tree
from sklearn.naive_bayes import GaussianNB

iris_dataset = load_iris()
print(iris_dataset)

FEATURES = iris_dataset.data
LABELS = iris_dataset.target
NAMES = iris_dataset.target_names

model = GaussianNB()

model.fit(FEATURES, LABELS)

known_data1 = [5.9, 3. , 5.1, 1.8]
known_data2 = [4.9, 3. , 1.4, 0.2]

predicted_targets = model.predict([known_data1, known_data2])
print(predicted_targets)

