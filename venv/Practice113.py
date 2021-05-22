import numpy as np
import pandas as pd
from sklearn import metrics
import matplotlib.pyplot as plt
import statsmodels.api as sm
from sklearn import svm
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

url_dataset = pd.read_csv('url_features.csv')
test_url = url_dataset['URL']
print(test_url)

train_X, test_X = train_test_split(url_dataset, test_size=0.2, random_state=1)

labels = train_X['malicious']
test_labels = test_X['malicious']
print("Split Complete")
count_train_classes = pd.value_counts(train_X['malicious'])
count_train_classes.plot(kind='bar', fontsize=16)
plt.xlabel("malicious")
plt.ylabel("malicious count")
#plt.show()

vectorizer = CountVectorizer()
count_X = vectorizer.fit_transform(url_dataset['URL'])

tVec = TfidfVectorizer()
count_X1 = tVec.fit_transform(url_dataset['URL'])

print("Vectorization complete")

test_count_X = vectorizer.transform(url_dataset['URL'])
test_Tfid_X = tVec.transform(url_dataset['URL'])
print("Vectorizing complete")

model = LogisticRegression(solver='lbfgs')
model.fit(count_X,labels)


