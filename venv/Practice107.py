"""
    Random Forest
    1. n -> How many decision trees to be used in our model
    2. Dataset shall be divided into n number of subsets.
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
"""
data_set = pd.read_csv("covid19-world.csv")
#print(data_set)

india_dataset = data_set[data_set['Country']=='India']
print(india_dataset)

X = india_dataset['Date']
Y = india_dataset['Confirmed']

print("DATE")
print(X)

print("Confirmed Cases")
print(Y)

plt.plot(X, Y)
plt.xlabel("Date")
plt.ylabel("Confirmed Cases")
plt.show()
"""
data_set = pd.read_csv("covid19-world.csv")
#print(data_set)

india_dataset = data_set[data_set['Country']=='India']
print(india_dataset)

X = india_dataset['Date'].values
confirmed_cases = india_dataset['Confirmed'].values
print(X)


days=[]


for date in X:
    #print(date)
    #print(pd.Period(date,freq='D').dayofyear)
    days.append(pd.Period(date,freq='D').dayofyear)

days = np.array(days)
print(days)

#plt.plot(days, confirmed_cases)
#plt.xlabel("Date")
#plt.ylabel("Confirmed Cases")
#plt.show()

model = RandomForestRegressor(n_estimators=100)

days = days[:, np.newaxis]
x_train, x_test, y_train, y_test = train_test_split(days, confirmed_cases, test_size=0.2, random_state=1)

model.fit(x_train,y_train)

y_pred = model.predict(x_test)

print("Original")
print(y_test)
print("Predicted")
print(y_pred)
