
board = []

for x in range (0, 9) :
    board.append(str(x + 1))

playerOneTurn = True
winner = False

def printBoard() :
    print( '\n -----')
    print( '|' + board[0] + '|' + board[1] + '|' + board[2] + '|')
    print( ' -----')
    print( '|' + board[3] + '|' + board[4] + '|' + board[5] + '|')
    print( ' -----')
    print( '|' + board[6] + '|' + board[7] + '|' + board[8] + '|')
    print( ' -----\n')

while not winner :
    printBoard()

    if playerOneTurn :
        print( "Player 1:")
    else :
        print( "Player 2:")

    try:
        choice = int(input(" "))
    except:
        print("please enter a valid field")
        continue
    if board[choice - 1] == 'X' or board[choice-1] == 'O':
        print("Aldready Played here. Try again!")
        continue

    if playerOneTurn :
        board[choice - 1] = 'X'
    else :
        board[choice - 1] = 'O'

    playerOneTurn = not playerOneTurn

    for x in range (0, 3) :
        y = x * 3
        if (board[y] == board[(y + 1)] and board[y] == board[(y + 2)]) :
            winner = True
            printBoard()
        if (board[x] == board[(x + 3)] and board[x] == board[(x + 6)]) :
            winner = True
            printBoard()

    if((board[0] == board[4] and board[0] == board[8]) or 
       (board[2] == board[4] and board[4] == board[6])) :
        winner = True
        printBoard()

print("Player " + str(int(playerOneTurn + 1)) + " wins!\n")

