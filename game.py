
##this is tic tac toe

px=True
py=False


board=[('*','A','B','C'), (1,'','',''),(2,'','',''),(3,'','','')]
print("Welcome to Tic Tac Toe. Below is the board. To move your piece, "
      "input a letter in caps followed by the number i.e. A1. Good Luck, and have fun.")

print()

for line in board:
    print(*line);

print()


print("player X, what's your first move?")
move=input()

def placement (move):
    if move[0]=='A':
        print (board[0,0])
