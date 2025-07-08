import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt

names = {
    'SSN': [2,5,6,9],
    'Name': ['Anaa','Bob','John','Mike']
}

ages = {
    'SSN': [1,2,4,3],
    'Age': [28,34,45,62]
}

df1 = pd.DataFrame(names)
df2 = pd.DataFrame(ages)

df = pd.merge(df1, df2, on="SSN", how='outer') #same as sql joins - left right outer innner
df.set_index('SSN', inplace=True)
print(df)