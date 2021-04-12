from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import numpy as np
import pandas as pd

table = pd.read_csv("advertising.csv")
#print(table)

# Data-Set
X = table.TV.values
Y = table.Sales.values

X = X.reshape((len(X), 1))
Y = Y.reshape((len(Y), 1))

model = LinearRegression()      # Creating model

model.fit(X,Y)    # Train model

Y1 = model.predict(X)  # Predictions
print(Y1)

score = r2_score(Y, Y1)  # Root mean square error
print(score)
