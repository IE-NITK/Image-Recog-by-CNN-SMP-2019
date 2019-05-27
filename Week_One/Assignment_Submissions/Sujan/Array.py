import numpy as np   

a=np.zeros((1,11))


a=(input("").split(" "))
m=int(a[0])
n=int(a[1])

b=np.reshape(a[2:],(m,n))
print(b)
