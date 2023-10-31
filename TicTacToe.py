board = ["-", "-", "-", 
        "-", "-", "-", 
        "-", "-", "-"]
currentPlayer = "X"
winner = None
gameRunning = True

#printing the game board
def printBoard(board):
    print(board[0] + "|" + board[2] + "|" + board[3])
    print("-----")
    print(board[3] + "|" + board[4] + "|" + board[5])
    print("-----")
    print(board[6] + "|" + board[7] + "|" + board[8])
printBoard(board)


#take player input
def playerInput(board): 
    inp = int(input("Enter a number 1-9: "))

    if inp >= 1 and inp <= 9 and board[inp-1] == "-":     #find out what this means
        board[inp-1] = currentPlayer
    else:
        print("Sorry, but this space is already taken")
     
#Check for win or tie
def checkHorizontal(board): 
    global winner
#switch the player

#check for win or tie again

 while gameRunning = True:
    printBoard(board)
    playerInput(board)