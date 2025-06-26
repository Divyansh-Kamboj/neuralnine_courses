import numpy as np 

x = np.array([
    [
    [1,2],
    [4,5],
    [14,15]

],

[
    [7,8],
    [10,11],
    [12,13]

],
[
    [7,8],
    [10,11],
    [12,13]

]
])

print(np.sqrt(x))
print(x.mean())
print(np.median(x))

print(x.size)
x = x.reshape(2,3,3)
print(x)
print(x.flatten())
print(x.transpose())