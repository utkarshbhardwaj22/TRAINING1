import numpy as np

array = np.genfromtxt("temperature.csv", delimiter = ",", dtype = np.string_)
#print(array)
for i in range(0,48471):
    print(array[i][6])