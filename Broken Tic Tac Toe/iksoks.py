board=[ [0,0,0],
        [0,0,0],
        [0,0,0],]

player=2




#draw the board
def draw():
    print("   0  1  2")
    for count, row in enumerate(board):
        print(count,row)

#check if placement is free
def isFree(row,column):
    if board[row][column]!=0:
        return False
    else:
        return True

#horizontal
def winh(game):
    for row in game:
        print(row)
        if row.count(row[0])==len(row) and row[0]!=0:
            return True

#vertical
def winv(game):
    for col in range(len(game)):
        check =[]
        for row in game:
            check.append(row[col])
        if check.count(check[0])==len(check) and check[0]!=0:
            return True

#diagonal
def wind(game):
    if game[0][0] == game[1][1] == game[2][2]!=0:
        return True
    if game[0][2] == game[1][1] == game[2][0]!=0:
        return True

def play(piece,row,column):
    if isFree(row,column):
        board[row][column]=piece
    else:
        print("Choose another")
        global player
        player=player-1
        

print("<",32*"-",">")
print()
pb=1
while pb==1:
    
    if player%2==0:
        if winh(board) or winv(board) or wind(board):
            print("Player 2 wins")
            pb=2
        else:
            draw()
            print("Choose placement")
            x=int(input("Select Row: "))
            y=int(input("Select Column: "))
            play(1,x,y)
    elif player%2!=0:
        if winh(board) or winv(board) or wind(board):
            print("Player 1 wins")
            pb=2
        else:
            draw()
            print("Choose placement")
            x=int(input("Select Row: "))
            y=int(input("Select Column: "))
            play(2,x,y)
    player+=1