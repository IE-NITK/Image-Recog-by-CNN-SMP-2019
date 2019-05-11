import numpy as np
x = [int(x) for x in input("").split()]
a = x[0]
b = x[1]
n = x[2 :]
c = np.reshape(n,(a,b))
print(c)
