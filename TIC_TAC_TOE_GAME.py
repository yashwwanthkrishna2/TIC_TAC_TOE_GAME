import random


board = ["*", "*", "*",
        "*", "*", "*",
        "*", "*", "*"]
currentPlayer = "X"
winner = None
gameRunning = True

# The first step is creating the game board.
def printBoard(board):
        
    print(board[1] + " | " + board[2] + " | " + board[3])
    print("---------")
    print(board[4] + " | " + board[5] + " | " + board[6])
    print("---------")
    print(board[7] + " | " + board[8] + " | " + board[9])


# The second step is making the player input.
def playerInput(board):
    inp = int(input("Select a spot 1-9: "))
    if board[inp-1] == "*":
        board[inp-1] = currentPlayer
    else:
        print("The spot is already occupied please pick another spot.")


# The third step is checking for win or tie.
def checkHorizontle(board):
    global winner
    if board[1] == board[2] == board[3] and board[1] != "*":
        winner = board[1]
        return True
    elif board[4] == board[5] == board[6] and board[4] != "-":
        winner = board[4]
        return True
    elif board[7] == board[8] == board[9] and board[7] != "-":
        winner = board[7]
        return True

def checkRow(board):
    global winner
    if board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[0]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "*":
        winner = board[2]
        return True
    elif board[3] == board[6] == board[9] and board[3] != "*":
        winner = board[3]
        return True


def checkDiag(board):
    global winner
    if board[1] == board[5] == board[9] and board[1] != "*":
        winner = board[1]
        return True
    elif board[3] == board[5] == board[7] and board[3] != "*":
        winner = board[3]
        return True


def checkIfWin(board):
    global gameRunning
    if checkHorizontle(board):
        printBoard(board)
        print(f"The winner is {winner}!")
        gameRunning = False

    elif checkRow(board):
        printBoard(board)
        print(f"The winner is {winner}!")
        gameRunning = False

    elif checkDiag(board):
        printBoard(board)
        print(f"The winner is {winner}!")
        gameRunning = False


def checkIfTie(board):
    global gameRunning
    if "-" not in board:
        printBoard(board)
        print("It is a tie!")
        gameRunning = False


# The fourth step is switching the player.
def switchPlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"


def computer(board):
    while currentPlayer == "O":
        position = random.randint(1, 9)
        if board[position] == "*":
            board[position] = "O"
            switchPlayer()


while gameRunning:
    printBoard(board)
    playerInput(board)
    checkIfWin(board)
    checkIfTie(board)
    switchPlayer()
    computer(board)
    checkIfWin(board)
    checkIfTie(board)


