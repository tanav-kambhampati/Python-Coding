#Review what "global" means in python. Also might wanna rework this cause its kinda copied by the yt video
# Global Variable makes the variable known to the whole program and not just one small section
board = ["-","-","-",
         "-","-","-",
         "-","-","-"]
player1 = "X"
winner = None
gameRunning = True

def print_board(board):
    print(board[0] + "|" + board[1] + "|" + board[2])
    print("-----")
    print(board[3] + "|" + board[4] + "|" + board[5])
    print("-----")
    print(board[6] + "|" + board[7] + "|" + board[8])

    print("Each space on the board corresponds to a number. This is the numbering:")
    print("1|2|3")
    print("4|5|6")
    print("7|8|9")

def move(board):
        player1_choice = int(input("Which place would you like to mark? Enter the number that corresponds to your space "))
        if player1_choice >= 1 and player1_choice <= 9 and board[player1_choice-1] == "-":
            board[player1_choice-1] = player1
        else:
            print("Sorry, somebody else is already in that spot. Try a different spot!")

def checkHorizontalwin(board):
    global winner 
    if board[0] == board[1] == board[2] and board[0] != "-":
        winner = board[0]
    if board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[4]
    if board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True 

def checkVerticalwin(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
    if board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[2]
    if board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]

def checkDiagonalwin(board):
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
    if board[6] == board[4] == board[2] and board[2] != "-":
        winner = board[6]

def checkTie(board):
    if "-" not in board:
        print_board(board)
        print("The game ended with a tie! Try playing again")
        gameRunning = False

def switchPlayer():
        global player1
        if player1 == "X":
            player1 = "O"
        else:
            player1 = "X"


while gameRunning == True:
    print_board(board)
    move(board)
    checkVerticalwin(board)
    checkHorizontalwin(board)
    checkDiagonalwin(board)
    checkTie(board)
    switchPlayer()
