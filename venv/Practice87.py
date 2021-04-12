from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import numpy as np

X = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
Y = np.array([1,4,9,16,25,36,49,64,81,100,121,144,169,196,225,256,289,324,361,400])

X = X.reshape((len(X),1))
Y = Y.reshape((len(Y), 1))

model = LinearRegression()

model.fit(X,Y)

Y1 = model.predict(X)
print(Y1)

score = r2_score(Y,Y1)
print(score)

unknown_value = [21]
predicted_value = model.predict([unknown_value])
print("The Precdicted value is: ",predicted_value)