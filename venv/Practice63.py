import numpy as np
import time


numbers = list(range(1,1000001))
time1 = time.time()
for i in numbers:
    pass
time2 = time.time()


array1 = np.array(numbers)
time3 = time.time()
for x in array1:
    pass
time4 = time.time()

print("Time stamp for List: ",time2-time1)
print()
print("Time stamp for numpy: ",time4-time3)
print()

num = [10,20,40,50,60,670,3,2,45,67,11,989,4534,423,42,126,64,1253,5732,276]
tim1= time.time()
print("The maximum from list: ", max(num))
tim2 = time.time()

tim3 = time.time()
arr = np.array(num)
print("Maximum from numpy array: ", np.max(num))
tim4 = time.time()

print("Time stamp for List: ", tim2-tim1)
print()
print("Time stamp for numpy array: ", tim4-time3)


