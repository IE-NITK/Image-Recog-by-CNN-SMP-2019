#INCOMPLETE PROGRAM
#RANDOM.CHOICE ERROR
import random,sys
list1=[' ']
for var in list(range(1,10)):
    list1.append(' ')
def reset():
    list1=[' ']
    for var in list(range(1,10)):
        list1.append(' ')
def struct(list1):
    print("--------------------------------------------------")
    for i in list(range(1,10)):
        if i==4 or i==7:
            print()
        if(i==1 or i==4 or i==7):
            print("  ",list1[i],'|' ,list1[i+1],'  |',list1[i+2])
            if(i is not 7):
                print(" ____ _____ ____")
    return
def smove():
    print(len(list1))
    print(list1.index(random.choice(list1)))
def start():
    c=random.choice([0,1])
    if(c==1):
        print("Computer will start")
        d=random.choice(["X","0"])
        if(d=="X"):
            e="0"
            smove()
        else:
            e="X"
            smove()
        struct(list1)
    else:
        d=input("Want \'0\' or \'X\'")
        if(d=="X"):
            e="0"
        else:e="X"
        print("Enter your first move")
        struct(list1)
print("Welcome to TicTacToe Game")
print("1. New Game\nPress any key to Exit")
def newGame():
    if (input()=="1"):
        start()
        while (True):
            y=input("Do you want to continue playing[y/n] following it press 1 if 'y '\n")
            if(y=="y"):
                newGame()
            else:sys.exit()
    else:sys.exit()
newGame()



        
