import numpy as np 
import matplotlib.pyplot as plt
from matplotlib import style 

x = np.arange(0,30,0.2)
y1 = np.sin(x)
y2 = np.cos(x)

style.use("dark_background")

plt.title("Sine Wave")
plt.xlabel("Weight of studnets")
plt.ylabel("Height of students")

plt.plot(x,y1, label="Sine")
plt.plot(x,y2, label="Cosine")
plt.legend(loc="upper right")

plt.show()