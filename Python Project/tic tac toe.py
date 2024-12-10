# Initialize 
board = ["-", "-", "-", 
         "-", "-", "-", 
         "-", "-", "-"] 
currentPlayer = "X" 
winner = None 
gameRunning = True 

# Print the game board
def printBoard(board):
    print(board[0] + "|" + board[1] + "|" + board[2])
    print(board[3] + "|" + board[4] + "|" + board[5])
    print(board[6] + "|" + board[7] + "|" + board[8])

# Player input function
def playerInput(board):
    try:
        inp = int(input("Enter a number 1-9: "))  
        if 1 <= inp <= 9 and board[inp - 1] == "-":
            board[inp - 1] = currentPlayer  
        else:
            print("Sorry, that spot is taken!")
    except ValueError:
        print("Please enter a valid number between 1 and 9.")

# Check horizontal for a win
def checkHorizontal(board):
    global winner
    for i in range(0, 9, 3): 
        if board[i] == board[i + 1] == board[i + 2] and board[i] != "-":
            winner = board[i]
            return True
    return False

# Check vertical for a win
def checkVertical(board):
    global winner
    for i in range(3):  
        if board[i] == board[i + 3] == board[i + 6] and board[i] != "-":
            winner = board[i]
            return True
    return False

# Check diagonal for a win
def checkDiagonal(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    if board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        return True
    return False

# Check for tie
def checkTie(board):
    if "-" not in board:
        return True
    return False

# Check for a win or tie
def checkWin():
    if checkHorizontal(board) or checkVertical(board) or checkDiagonal(board):
        return True
    return False

# Switch player
def switchPlayer():
    global currentPlayer
    currentPlayer = "O" if currentPlayer == "X" else "X"

# Main game loop
while gameRunning:
    printBoard(board)
    playerInput(board)
    
    if checkWin():
        printBoard(board)
        print(f"Player {winner} wins the game!")
        gameRunning = False
        break
    elif checkTie(board):
        printBoard(board)
        print("Oh no, It's a tie!")
        gameRunning = False
        break
    switchPlayer() 
