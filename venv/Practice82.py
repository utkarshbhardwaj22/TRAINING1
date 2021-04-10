import pandas as pd
import numpy as np

data = np.random.randn(5,4)
print(data)

table = pd.DataFrame(data= data, columns=["col1", "col2", "col3", "col4"])
print(table)

print()
print("Iterate data of table")
for key, value in table.iteritems():
    print("=======================")
    print(key)
    print()
    print(value)

for key, value in table.iterrows():
    print("=======================")
    print(key)
    print()
    print(value)

for row in table.itertuples():
    print("=======================")
    print(row)