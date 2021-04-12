from scipy import stats
import numpy as np
import matplotlib.pyplot as plt

X = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
Y = [1,4,9,16,25,36,49,64,81,100,121,144,169,196,225,256,289,324,361,400]

data = stats.linregress(X, Y)
print(data,type(data))

max_x = np.max(X) + 10
min_y = np.min(Y) - 10

print(max_x)
print(min_y)

x = np.linspace(min_y, max_x, 100)
y = data[1] + data[0] * x

print(x)
print(y)

plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.grid(True)
plt.plot(x, y, color="red", label="Regression Line")
plt.scatter(X,Y, color="green", label="Data Points")
plt.legend()
plt.show()
