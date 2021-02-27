data_27 = [145,6477,3628,4122,6232]
data_28 = [123,567,876,2576,4546]

def max_cases(data):
    max = data[0]

    for i in range(1,len(data)):
        if data[i] > max:
            max = data[i]

    return max

print("Maximum of 27:",max_cases(data_27))
print("Maximum of 28:",max_cases(data_28))




