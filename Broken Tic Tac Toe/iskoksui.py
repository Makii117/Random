import numpy as np
import pygame 
import sys
pygame.init()
pygame.font.init()
board=[ [0,0,0],
        [0,0,0],
        [0,0,0],]

player=2
display=(300,300)
RED=(255,0,0)
BLUE=(0,0,255)
WHITE=(255,255,255)
SQUARESIZE=100
RADIUS=30
BLACK=(0,0,0)
font=pygame.font.SysFont("monospace",30)


def DrawLines(screen):
    pygame.draw.line(screen,WHITE,(100,0),(100,300))
    pygame.draw.line(screen,WHITE,(200,0),(200,300))
    pygame.draw.line(screen,WHITE,(0,100),(300,100))
    pygame.draw.line(screen,WHITE,(0,200),(300,200))

def iks(screen,x,y,width=4):
    pygame.draw.rect(screen,RED,(int(x*SQUARESIZE+50), int(y*SQUARESIZE+50),RADIUS,RADIUS),width)

def oks(screen,x,y,width=4):
    pygame.draw.circle(screen, BLUE,(int(x*SQUARESIZE+50), int(y*SQUARESIZE+50)),RADIUS,width)




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
    elif isFree(row,column)==False:
        print("Choose another")
        global player
        player=player-1
        boardClear(board,screen)
def boardClear(board,screen):
    for i in range(0,3):
        for j in range(0,3):
            board[i][j]=0
    screen.fill(BLACK)
    DrawLines(screen)
    draw()



screen=pygame.display.set_mode(display)
DrawLines(screen)

pygame.display.update()




pb=1
while pb==1:
    for event in pygame.event.get():  
        if event.type==pygame.QUIT:
                sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if player%2==0:
                if winh(board) or winv(board) or wind(board):
                    print("Player 2 wins")
                    label=font.render("Player 2 wins",1,BLUE)
                    screen.blit(label,(40,10)) 
                    pygame.display.update()
                    pb=2
                elif event.type==pygame.MOUSEBUTTONDOWN:
                    x1=(pygame.mouse.get_pos()[0])
                    y1=(pygame.mouse.get_pos()[1])
                    print(x1,y1)
                    x=x1//100
                    y=y1//100
                    print(x,y)
                    play(1,y,x)
                    iks(screen,x,y)
                    pygame.display.update()
                else:
                    boardClear(board)
            elif player%2!=0:
                if winh(board) or winv(board) or wind(board):
                    print("Player 1 wins")
                    label=font.render("Player 1 wins",1,RED)
                    screen.blit(label,(40,10))
                    pygame.display.update()
                    pb=2
                elif event.type==pygame.MOUSEBUTTONDOWN:
                    x1=(pygame.mouse.get_pos()[0])
                    y1=(pygame.mouse.get_pos()[1])
                    x=x1//100
                    y=y1//100
                    print(x,y)
                    play(2,y,x)
                    oks(screen,x,y)
                    pygame.display.update()
                else:
                    boardClear(board,screen)
            player+=1