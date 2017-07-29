import numpy as np
a=np.random.randint(low=1, high=1000, size=100)
print(a)
A=a.reshape(10,10)
print(A)
b=np.amax(a)
print(b)
c=np.amin(a)
print(c)