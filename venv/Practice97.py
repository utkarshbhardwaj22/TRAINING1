from sklearn.datasets import load_iris
from sklearn import tree
from sklearn import metrics  # Accuracy Scores
from sklearn.model_selection import train_test_split # Break dataset randomly into training and testing

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

x_train, x_test, y_train, y_test = train_test_split(features, labels, test_size=0.3, random_state=1)

print(x_train)
print(y_train)
print(len(x_train), len(y_train))

print()
print(x_test)
print(y_test)
print(len(x_test), len(y_test))


model = tree.DecisionTreeClassifier()

model.fit(x_train, y_train)

y_pred = model.predict(x_test)
accuracy = metrics.accuracy_score(y_test, y_pred)
print("ACCURACY = ", accuracy)

known_iris1 = [5.1, 3.5, 1.4, 0.2]
known_iris2 = [7.4, 2.8, 6.1, 1.9]

predicted_labels = model.predict([known_iris1, known_iris2])
#print(predicted_labels)