import numpy as np
import pandas as pd
from sklearn import metrics
import matplotlib.pyplot as plt
import statsmodels.api as sm
from sklearn import svm
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

url_dataset = pd.read_csv('url_features.csv')
#print(url_dataset)
data_features = url_dataset[['token_count','rank_host','ASNno','sec_sen_word_cnt','avg_token_length','No_of_dots','Length_of_url',
                            'avg_path_token','IPaddress_presence','Length_of_host','safebrowsing','avg_domain_token_length','path_token_count',
                            'largest_domain','domain_token_count','largest_path','largest_token']]





data_labels = url_dataset['malicious']

label = ['Safe', 'Unsafe', 'Malicious']

x_train, x_test, y_train, y_test = train_test_split(data_features, data_labels, test_size=0.2, random_state=1)


#model = svm.SVC()
#model = DecisionTreeClassifier()
model = RandomForestClassifier(n_estimators=100)

model.fit(x_train, y_train)

y_pred = model.predict(x_test)

for x in y_pred:
    print(label[y_pred[x]])
    x=+1

accuracy = metrics.accuracy_score(y_test, y_pred).round(2)*100
print(accuracy)




