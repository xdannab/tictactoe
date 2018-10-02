
##this is tic tac toe


board=[['*','A','B','C'], [1,'_','_','_'],[2,'_','_','_'],[3,'_','_','_']]
        
def view(board):
    for line in board:
        print(*line);
 
def yplacement(move):
    if move[0]=='A':
        y=1
    elif move[0]=='B':
        y=2
    elif move[0]=='C':
        y=3
    else:
        move=input("incorrect input letter, try again.")
        placement(move)
    return y

def xplacement(move):
    if move[1]=='1':
        x=1
    elif move[1]=='2':
        x=2
    elif move[1]=='3':
        x=3
    else:
        move=input("incorrect input num, try again.")
        placement(move)
    return x

  
def placement(move, player):
    y=yplacement(move)
    x=xplacement(move)
    board[x][y]=player
    view(board)
    changeplayer(player)

def changeplayer(player):
    if player=='X':
        player='O'
    return player

def game():
    player='X'
    for i in range (10):
        move=input("\n"+"player " +player+", what's your move?"+"\n")
        placement(move,player)


        

        


print("Welcome to Tic Tac Toe. Below is the board. To move your piece, "
      "input a letter in caps followed by the number i.e. A1. Good Luck, and have fun."+"\n")

view(board)
game()
