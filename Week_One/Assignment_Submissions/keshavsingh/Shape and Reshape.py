import numpy as np
x = list(map(int, input("Enter m,n,m x n intgers ").split()))
m,n=x[0],x[1]
del x[0],x[0]
if (m==3 and n==3 ) or (m==1 and n==9) or (m==9 and n==1):
    if m==1:
        a=np.array(x)
    elif m==3:
        a=np.reshape(x, (3, 3))
        print(a)
    elif m==9:
        a=np.reshape(x,(9,1))
        print(a)
