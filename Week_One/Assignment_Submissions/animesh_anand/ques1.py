import numpy as np
import random

board = np.full((9, )," ")
list = np.array([1,2,3,4,5,6,7,8,9])

i=0
flag = 2

while i<5 :
  n = int(input("Enter a number between 1 to 9 where you will place your 'x'"))
  board[n-1] = 'x'
  index = np.argwhere(list == n)
  list = np.delete(list, index)
  c = np.reshape(board,(3,3))
  print(c)
  for x in range (0, 3) :
        y = x * 3
        if (board[y] == board[(y + 1)]== 'x' and board[y] == board[(y + 2)] == 'x') :
            flag = 1
        if (board[x] == board[(x + 3)] == 'x' and board[x] == board[(x + 6)] == 'x') :
            flag = 1
        if((board[0] == board[4] == board[8] == 'x') or
          (board[2] == board[4] == board[6] == 'x')) :
            flag = 1

  if flag == 1 :
    print("You win")
    break

  if list.size == 0 :
    print("No result")
    break

  m = np.random.choice(list)
  board[m-1] = 'o'
  index1 =  np.argwhere(list == m)
  list = np.delete(list, index1)
  d = np.reshape(board,(3,3))
  print(d)

  for x in range (0, 3) :
        y = x * 3
        if (board[y] == board[(y + 1)]== board[(y + 2)] == 'o') :
            flag =0
        if (board[x] == board[(x + 3)] == board[(x + 6)] == 'o') :
            flag =0
        if((board[0] == board[4] == board[8] == 'o') or
          (board[2] == board[4] == board[6] == 'o')) :
            flag =0

  if flag == 0:
    print("You lose")
    break

  i=i+1

 
