import numpy as np
import pandas as pd

odd_numbers = np.arange(1,100,2)
even_numbers = np.arange(0,100,2)

numbers = {"ODD Numbers": odd_numbers,
           "EVEN Numbers": even_numbers}
print(numbers)

table = pd.DataFrame(numbers)
print(table)
print("Sum of the table:")
print(table.sum())

print("Max of the table:")
print(table.max())

print("Min of the table:")
print(table.min())

print("Std of the table:")
print(table.std())