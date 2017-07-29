import numpy as np
import matplotlib. pyplot as plt
x = [0,1,2,3,4,5,6,7,8,9]
y=[1,3,2,5,7,8,8,9,10,12]
a=np.mean(x)
b=np.mean(y)
print(a,b)
slope=np.sum((x-a)*(y-b))/np.sum((x-a)*(x-a))
print(slope)
intercept=b-slope*a
print(intercept)
z=slope*x+intercept
plt. plot (x , z)
plt.plot(x,y)
plt.show()
