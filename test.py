
def placement( player):
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
