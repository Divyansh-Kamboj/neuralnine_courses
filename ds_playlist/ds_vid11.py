import numpy as np 
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

plt.figure(1)
ax = plt.axes(projection='3d')

z = np.linspace(0,30, 100)
x = np.sin(z)
y = np.cos(z)

ax.plot3D(x,y,z)

plt.figure(2)
ax2 = plt.axes(projection="3d")

def c_func(x,y):
    return np.sin(np.sqrt(x ** 2 + y ** 2))

a = np.linspace(-5,5,100)
b = np.linspace(-5,5,100)

A, B = np.meshgrid(a,b)
C = c_func(A,B)

ax2.plot_surface(A,B,C)

plt.show()