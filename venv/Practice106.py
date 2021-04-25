import numpy
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

data_set = pd.read_csv('speeds.csv')
print(data_set)

X = data_set['hour'].values
Y = data_set['speed'].values
"""
model = np.poly1d(np.polyfit(X, Y, 3))
line = np.linspace(1, len(X), 100)
poly_data = model(line)
print(poly_data)

plt.scatter(X, Y,color='red', marker='o')
plt.plot(line, poly_data)
plt.show()
"""

# for sklearn we need data in 2d shape

X = X[:, numpy.newaxis]
Y = Y[:, numpy.newaxis]
print(X)
print(Y)

poly_features = PolynomialFeatures(degree=2)
poly_X = poly_features.fit_transform(X)

model = LinearRegression()

model.fit(poly_X, Y)
Y_pred = model.predict(poly_X)

hour = np.array([16])
hour = hour.reshape(len(hour), 1)
hour_input = poly_features.fit_transform(hour)

predicted_speed = model.predict(hour_input)
print(predicted_speed)
