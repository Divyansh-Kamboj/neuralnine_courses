import pandas as pd 
import matplotlib.pyplot as plt

s1 = pd.Series([1,2,3,4,5,1,4,2], ['a','b','c','d','e','f','g','h'])

s1.plot.pie() #can use any kind of matplotlib graphs
plt.show()

s1.to_csv('myseries.csv') #can be used on all different kinds of files 