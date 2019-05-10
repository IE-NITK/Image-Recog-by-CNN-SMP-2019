#!/usr/bin/env python
# coding: utf-8

# In[23]:


import  numpy as np
m=int(input())
n=int(input())
thislist=[]
for x in range(m*n):
    y=input()
    thislist.insert(x,y)
a=np.array([thislist])
a=a.reshape(m,n)
print(a)


# In[12]:


thislist=[1,2,3,4,5,6,7,8,9]
print(thislist[6:])


# In[ ]:




