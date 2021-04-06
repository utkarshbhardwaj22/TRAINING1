"""
Matplotlib -> Data visualization in graphical form
"""
import matplotlib.pyplot as plt

X = list(range(0,20))
y1 = [x*10 for x in X]
y2 = [x*x for x in X]
y3 = [x*x*x for x in X]

plt.plot(X, label= "X")
plt.plot(X,y1, label= "y1")
plt.plot(X,y2, label= "y2")
plt.plot(X,y3, label= "y3")

plt.legend() # for showing the label
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.title("Practice line graph")

plt.grid()

plt.show()

