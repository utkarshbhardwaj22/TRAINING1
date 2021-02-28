"""
List comprehensions

"""

numbers=[10,20,30,40]

print(numbers)
square_numbers=[x*x for x in numbers]
print(square_numbers)

prices=[1200, 3400, 1245, 5700]
discounted_price=[0.5*x for x in prices if x>1500]
print("Discounted Prices:",discounted_price)