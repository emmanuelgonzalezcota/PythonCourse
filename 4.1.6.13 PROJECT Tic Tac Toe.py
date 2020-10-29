# the function accepts one parameter containing the board's current status
# and prints it out to the console
def DisplayBoard(board):
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|  ",board[0][0],"  |  ",board[0][1],"  |  ",board[0][2],"  |")
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|  ",board[1][0],"  |  ",board[1][1],"  |  ",board[1][2],"  |")
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|  ",board[2][0],"  |  ",board[2][1],"  |  ",board[2][2],"  |")
    print("|       |       |       |")
    print("+-------+-------+-------+")

# the function accepts the board current status, asks the user about their move, 
# checks the input and updates the board according to the user's decision
def EnterMove(board):
    O=int(input("Enter your move:"))
    while(O > 0 and O < 10):
        if   (O==1): 
            if (0,0) in MakeListOfFreeFields(board): board[0][0]='O'
            else: 
                print("Spot occupied!")
                EnterMove(board)
        elif (O==2): 
            if (0,1) in MakeListOfFreeFields(board): board[0][1]='O'
            else: 
                print("Spot occupied!")
                EnterMove(board)        
        elif (O==3):
            if (0,2) in MakeListOfFreeFields(board): board[0][2]='O'
            else: 
                print("Spot occupied!")
                EnterMove(board)
        elif (O==4):
            if (1,0) in MakeListOfFreeFields(board): board[1][0]='O'
            else: 
                print("Spot occupied!")
                EnterMove(board)
        elif (O==5):
            if (1,1) in MakeListOfFreeFields(board): board[1][1]='O'
            else: 
                print("Spot occupied!")
                EnterMove(board)        
        elif (O==6):
            if (1,2) in MakeListOfFreeFields(board): board[1][2]='O'
            else: 
                print("Spot occupied!")
                EnterMove(board)        
        elif (O==7):
            if (2,0) in MakeListOfFreeFields(board): board[2][0]='O'
            else: 
                print("Spot occupied!")
                EnterMove(board)          
        elif (O==8):
            if (2,1) in MakeListOfFreeFields(board): board[2][1]='O'
            else: 
                print("Spot occupied!")
                EnterMove(board)         
        elif (O==9):
            if (2,2) in MakeListOfFreeFields(board): board[2][2]='O'
            else: 
                print("Spot occupied!")
                EnterMove(board)
        break        
    else:
        print("Wrong spot! Must be between 1 and 9")        
        EnterMove(board)
    DisplayBoard(board)
    VictoryFor(board, 'O')
    return board


# the function browses the board and builds a list of all the free squares; 
# the list consists of tuples, while each tuple is a pair of row and column numbers
def MakeListOfFreeFields(board):
    FreeFieldsList=[]
    for row in range(0,3):
        for column in range(0,3):
            if type(board[row][column]) == int:
                FreeFieldsList.append((row,column))
    return FreeFieldsList                

# the function analyzes the board status in order to check if 
# the player using 'O's or 'X's has won the game
def VictoryFor(board, sign):
    if sign =='X':
        for i in range(0,3):
            if(board[i].count('X') == 3): winnerFunction(board,'X')
            if board[0][i]=='X' and board[1][i]=='X' and board[2][i]=='X': winnerFunction(board,'X')
        if board[0][0]=='X' and board[1][1]=='X' and board[2][2]=='X': winnerFunction(board,'X')
        if board[2][0]=='X' and board[1][1]=='X' and board[0][2]=='X': winnerFunction(board,'X')
    else:
        for i in range(0,3):
            if(board[i].count('O') == 3): winnerFunction(board,'O')
            if board[0][i]=='O' and board[1][i]=='O' and board[2][i]=='O': winnerFunction(board,'O')
        if board[0][0]=='O' and board[1][1]=='O' and board[2][2]=='O': winnerFunction(board,'O')
        if board[2][0]=='O' and board[1][1]=='O' and board[0][2]=='O': winnerFunction(board,'O')
    return board 


# the function draws the computer's move and updates the board
def DrawMove(board):
    from random import randrange
    Xpos=randrange(len(MakeListOfFreeFields(board)))-1
    X=MakeListOfFreeFields(board)
    board[X[Xpos][0]][X[Xpos][1]] = 'X'
    print("   TIC  -  TAC  -  TOE   ")
    DisplayBoard(board)
    VictoryFor(board, 'X')
    return board

#Winner Function
def winnerFunction(board,sign):
    FreeFieldsList=MakeListOfFreeFields(board)
    for field in FreeFieldsList:
        board[field[0]][field[1]] = '-'
    DisplayBoard(board)
    if sign == 'X': print("  Computer Won :(")
    else: print("    YOU WON !  ")
         

# Main Code
board = [[1,2,3],[4,'X',6],[7,8,9]]
print("   TIC  -  TAC  -  TOE   ")
DisplayBoard(board)
cc=0
while cc < 8 and len(MakeListOfFreeFields(board)) > 0:
    if cc % 2:
        DrawMove(board)
    else:
        EnterMove(board)
    cc +=1
#if cc==8: print("It´s a Draw") 
#dRAW ACTIVATES IF SOMEBODY WIND IN LAST MOVE