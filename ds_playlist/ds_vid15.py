import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt

data = {
    'SSN': [123,567,890,234],
    'Name': ["Anna", 'Bob', 'Bob', 'Tyler'],
    'Age': [24,32,22,45],
    'Height': [165,173,180,170]
}

df = pd.DataFrame(data)
df.set_index("SSN", inplace=True)

print(df['Height'].apply(np.sin))

for keys, value in df.items():
    print("{}: {}".format(keys,value))

df.sort_index(inplace=True)
print("")
print(df)

df.sort_values(by=["Age", "Name"], inplace=True)
print("")
print(df)