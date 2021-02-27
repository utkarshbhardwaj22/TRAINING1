number = [24,20,109,22,8,60]

print("Before:", number)

n = len(number)


for i in range(n):
    for j in range(n-i-1):
        if number[j] > number[j+1]:
            number[j], number[j+1] = number[j+1],number[j]

print("After:", number)