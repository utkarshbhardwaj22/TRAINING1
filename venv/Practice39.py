# MAP function ->  a built in function in python

#ob1 = lambda amount: amount- 0.20*amount

list_of_prices= [100, 200, 300, 400, 500]

#result = map(ob1, list_of_prices)

result = map(lambda amount: amount- 0.20*amount, list_of_prices)
print(list(result))

# for flat 50% off
result1 = map(lambda price: price/2, list_of_prices)
print(list(result1))

# filter function
print()
print(list(filter(lambda price: price/2, list_of_prices)))


# reduce function
from functools import reduce
ob1 = lambda x, y: x+y
price = [1,2,3,4]
result = reduce(ob1, price)
print(result)