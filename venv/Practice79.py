"""
Pandas
    series -> 1d array
    dataframe -> 2d array(table)
"""

import numpy as np
import pandas as pd

array1 = np.arange(1, 101, 2)
array2 = list(range(1, 101, 2))

print(array1)
print(array2)

S1 = pd.Series(array1)
S2 = pd.Series(array2)

print(S1)
print()
print(S2)

print(S1.axes)
print(S1.values)
print(S1.head()) # first 5 records
print(S1.tail()) # last 5 records
print(S1.head(10)) # first 10 records
print(S1.tail(10)) # last 10 records
