import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt

df = pd.read_csv('people.csv', delimiter=',')
df.set_index('SSN', inplace=True)

print(df.loc[(df["Age"] >= 40) & (df["Height"] > 170)]["Name"])
