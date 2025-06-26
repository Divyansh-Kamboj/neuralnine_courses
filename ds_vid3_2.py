import numpy as np

a = np.array([
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
])

b = np.array([
    [10,20,30,40],
    [50,60,70,80],
    [90,100,110,120]
])

c = np.concatenate((a,b))
print(c.shape)
c2 = np.stack((a,b))
print(c2.shape)

x = np.random.randint(0,10, size=(4,4))
print(np.split(x, 2))
print(np.hsplit(x,2))

y = [1000,2000,3000,4000]

a = np.insert(a,1,y,axis=0)
print(a)
b = np.append(b,[y], axis=0)
print(b)