import numpy as np

user_input = input()
list1 = user_input.split(" ")
m = int(list1[0])
n = int(list1[1])

array = np.array(list1[2:])

print(array.reshape(m,n))

