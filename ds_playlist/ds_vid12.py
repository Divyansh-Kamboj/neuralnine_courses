import pandas as pd
import matplotlib.pyplot as plt

series = pd.Series([10,20,30,40],['A', 'B', 'C', 'D'])

series.name = "My series"

s1 = pd.Series([1,2,3,4], ['a','b','c','d'])
s2 = pd.Series([7,5,1,2], ['c','b','a','d']) #positions are not relavent it adds values of each inddex

print(series['C'])
print(series.iloc[0])
print(s1+s2)

print(s1.head(1))
print(s1.tail(2))

def mysquare(x):
    return x**2

print(s1.apply(mysquare))

print(s2.sort_index()) #sort_value does the same for values

s2.sort_values(inplace=True) #actually redefines the s2 series with the sorted verison