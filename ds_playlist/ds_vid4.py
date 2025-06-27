import numpy as np 
import matplotlib.pyplot as plt

x = np.arange(-100,101,1)
y1 = 0.5 * x ** 2 + 2 * x
y2 = np.sin(x) * 2000
y3 = np.cos(x) * 2000

plt.plot(x,y1, 'r--')
plt.plot(x,y2, 'b')
plt.plot(x,y3, 'go')
plt.show()