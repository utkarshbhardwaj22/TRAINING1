import matplotlib.pyplot as plt
from sklearn import datasets,svm
from sklearn.model_selection import train_test_split
from sklearn import metrics

digits = datasets.load_digits()

FEATURES = digits.data
LABELS = digits.target

print(digits.target_names)


x_train, x_test, y_train, y_test = train_test_split(FEATURES, LABELS, test_size=0.2, random_state=1)

model = svm.SVC()

model.fit(x_train, y_train)

y_pred = model.predict(x_test)
print(y_pred)


score = metrics.accuracy_score(y_test,y_pred)
print(score)

predicted_label = model.predict([FEATURES[99]])
print(predicted_label)