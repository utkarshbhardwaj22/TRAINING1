import matplotlib.pyplot as plt
"""
A = [1,2,3,4,5,6]
B = [7,8,9,4,5,8]

#plt.bar(A,B)
#plt.hist(A, 20)
plt.barh(A,B)
plt.show()
"""

highest_scores = {"Sachin": 200, "Rohit": 264, "MS Dhoni": 183, "Virat": 183, "Sehwag": 219}

#plt.bar(0, highest_scores["Sachin"])
#plt.bar(1, highest_scores["Rohit"])
#plt.bar(2, highest_scores["MS Dhoni"])
#plt.bar(3, highest_scores["Virat"])
#plt.bar(4, highest_scores["Sehwag"])

#plt.show()

for i,key in enumerate(highest_scores):
    print(i,key,highest_scores[key])
    plt.barh(key, highest_scores[key])

plt.show()