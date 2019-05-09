import numpy as np
import random
b=np.zeros((3,3))
l=[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
store=np.zeros((9,1))
k=1;
for i in range(3):
    for j in range(3):
        b[i][j]=k
        k+=1
def show():
    print(" _____")
    for i in range(3):
        print ("|%s|%s|%s|"%(l[i][0],l[i][1],l[i][2]))
        print (" _____")


        
        
show()     
st=0
ast=0
while(True):
    inp=int(input("which tile do you want to put your x in?"))
    for i in range(3):
        for j in range(3):
            if b[i][j]==inp:
                l[i][j]="X"
                store[st]=inp
                st+=1
    show()
    f=0
    co=0
    
    for i in range(3):
        k=0
        if(l[:][i]==["X",'X',"X"]) :
            
            f=1
            break
        if(l[0][i]=="X" and l[1][i]=="X" and l[2][i]=="X"):
            f=1
            break
        
        
    if(l[0][0]=='X' and l[1][1]=='X' and l[2][2]=='X') :
        f=1
    elif(l[0][2]=="X" and l[1][1]=='X' and l[2][0]=="X"):
        f=1
    if(f==1):
        print ("you win")
        ast=1
        break
    
    print("My turn")
    
    while(True):
        co=random.randint(1,10)
        if co not in store:
            break
    print (co)
    for i in range(3):
        for j in range(3):
            if (b[i][j]==co):
                l[i][j]="O"
                store[st]=co
                st+=1 
    show()
    for i in range(3):
        if(l[:][i]==["O",'O',"O"] ):
            print ("I win")
            f=1
            break
        if(l[0][i]=="O" and l[1][i]=="O" and l[2][i]=="O"):
            f=1
            break
    if(l[0][0]=='O' and l[1][1]=='O' and l[1][1]=='O') :
        f=1
    elif(l[0][2]=="X" and l[1][1]=='X' and l[2][0]=="X"):
        f=1
        
    if(f==1):
        print ("I win")
        ast=2
        break
        
    if(st==9):
        break   

file=open('Score','a')

if(ast==1):
    file.write("\nGame won by you")
elif(ast==2):
    file.write("\nGame won by me")
else:
    print('draw')
    file.write("\nGame drew")

    
    

    


    

