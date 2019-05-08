import numpy as np

numberlist = np.array(range(9))
board = np.full((9, ), " ")
file = open("game.txt", 'a+')
file.write("Game is saved as number of square 0 being first 8 being last see board below : \n")
file.write("0 | 1 | 2 \n" + "--------- \n")  #drawing board
file.write("3 | 4 | 5 \n" + "--------- \n")
file.write("6 | 7 | 8 \n" + "--------- \n")

while True:
    a = int(input("Your turn with(o) enter a number to do your move.(0-8)"))
    print(type(a))
    numberlist = np.delete(numberlist, np.argwhere(numberlist == a))
    board[a] = '0'
    print(board.reshape(3, 3))
    file.write("user: " + str(a) + "\n")
    if np.array_equal(board[0:3], np.array(['0', '0', '0'])) or np.array_equal(board[3:6], np.array(['0', '0', '0'])) or np.array_equal(board[6:9], np.array(['0', '0', '0'])) or np.array_equal(board[0:7:3], np.array(['0', '0', '0'])) or np.array_equal(board[1:8:3], np.array(['0', '0', '0'])) or np.array_equal(board[2:9:3], np.array(['0', '0', '0'])) or np.array_equal(board[0:9:4], np.array(['0', '0', '0'])) or np.array_equal(board[2:8:2], np.array(['0', '0', '0'])) :
        print("you win")
        file.write("user wins" + "\n"*3)
        break
    if numberlist.size == 0:
        print("Draw")
        file.write("Draw" + "\n"*3)
        break
    a = np.random.choice(numberlist)
    numberlist = np.delete(numberlist, np.argwhere(numberlist == a))
    board[a] = '1'
    file.write("Computer: " + str(a) + "\n")
    print(board.reshape(3, 3))
    if np.array_equal(board[0:3], np.array(['1', '1', '1'])) or np.array_equal(board[3:6], np.array(['1', '1', '1'])) or np.array_equal(board[6:9], np.array(['1', '1', '1'])) or np.array_equal(board[0:7:3], np.array(['1', '1', '1'])) or np.array_equal(board[1:8:3], np.array(['1', '1', '1'])) or np.array_equal(board[2:9:3], np.array(['1', '1', '1'])) or np.array_equal(board[0:9:4], np.array(['1', '1', '1'])) or np.array_equal(board[2:8:2], np.array(['1', '1', '1'])) :
        print("Computer wins")
        file.write("Computer wins" + "\n" * 3)
        break


file.close()



