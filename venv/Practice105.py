"""
    Polynomial Regression

"""
import matplotlib.pyplot as plt
import numpy


X = list(range(1, 21))
print(X)

Y = [40,50,60,60,32,141,45,96,24,78,32,14,55,46,23,72,66,99,100,125]
print(Y)

model = numpy.poly1d(numpy.polyfit(X, Y, 3))
line = numpy.linspace(1, 20, 100)
poly_data = model(line)
print(poly_data)

plt.scatter(X, Y,color='red', marker='o')
plt.plot(line, poly_data)
plt.show()

