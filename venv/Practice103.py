"""
    Multiple Linear Regression
"""

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics
import statsmodels.api as sm


data_set = pd.read_csv("company.csv")
print(data_set)


"""
#Tip: Must check the dataset linearity

plt.scatter(data_set['R&D Spend'], data_set['Profit'])
plt.title("R&D Spend vs Profit", fontsize=14)
plt.xlabel("R&D Spend", fontsize=14)
plt.ylabel("Profit", fontsize=14)
plt.grid(True)
plt.show()

plt.scatter(data_set['Marketing Spend'], data_set['Profit'])
plt.title("Marketing Spend vs Profit", fontsize=14)
plt.xlabel("Marketing Spend", fontsize=14)
plt.ylabel("Profit", fontsize=14)
plt.grid(True)
plt.show()
"""

X = data_set[['R&D Spend', 'Marketing Spend']]
Y = data_set['Profit']

print(X)
print()
print(Y)

model = LinearRegression()

x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=1)

model.fit(x_train,y_train)

y_pred = model.predict(x_test)


print("interceptor: ", model.intercept_)
print("coefficients: ", model.coef_)

RnD_Spend = 165349.2
M_Spend = 471784.1

predicted_profit = model.predict([[RnD_Spend, M_Spend]])
print(predicted_profit)

print("~~~~~~~~~ STATSMODEL API ~~~~~~~~~")

# Creating and training the model using statsmodel
#stats_model = sm.OLS(Y,X).fit()
#stats_model = sm.GLS(Y,X).fit()
stats_model = sm.WLS(Y,X).fit()
stats_model_summary = stats_model.summary()
print(stats_model_summary)

predictions = stats_model.predict(X)
print(predictions)


