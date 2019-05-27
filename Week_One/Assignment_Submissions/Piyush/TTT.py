import numpy as np
import random
import sys
a=np.array([['','',''],['','',''],['','','']])
for i in range(5):
    while True:
        print("Specify row and column number for your move:")
        p=int(input())
        q=int(input())
        if a[p][q]=='':
            a[p][q]='x'
            print(a)
            break
    if i!=4:
        while True:
            c=random.randint(0,2)
            d=random.randint(0,2)
            if a[c][d]=='':
                a[c][d]='o'
                print(a)
                break
     
print('finished')
t=0
m=0
for x in range(3):
    for y in range(3):
        if a[x][y]=='x':
            t=t+1
        if a[x][y]=='o':
            m=m+1
    if t==3:
        print('Player won!')
        sys.exit()
    if m==3:
        print('computer won!')
        sys.exit()
    t=0
    m=0
t=0
m=0
for x in range(3):
    for y in range(3):
        if a[y][x]=='x':
            t=t+1
        if a[y][x]=='o':
            m=m+1
    if t==3:
        print('Player won!')
        sys.exit()
    if m==3:
        print('computer won!')
        sys.exit()
    t=0
    m=0
if a[0][0]==a[1][1]==a[2][2] =='x':
    print('Player won!')
    sys.exit()
if a[0][0]==a[1][1]==a[2][2] =='o':
    print('Computer won!')
    sys.exit()
if a[0][2]==a[1][1]==a[2][0] =='x':
    print('Player won!')
    sys.exit()
if a[0][2]==a[1][1]==a[2][0] =='o':
    print('Computer won!')
    sys.exit()
m=1
if m==1:
    print('Game tied!')