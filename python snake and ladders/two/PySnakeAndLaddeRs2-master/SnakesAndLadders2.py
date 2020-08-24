#made by Rushi

from sys import exit as quit
from Classes import *

import pygame,time,random
from pygame.locals import *


pygame.init()

display_width = 900
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Snakes And LaddeRs')
black = (0,0,0)
white = (255,255,255)
start = True
pl = 0
k = 101
p = 0
dice = 0
clock = pygame.time.Clock()
startimg = pygame.image.load('start_page.png')
startimg = pygame.transform.scale(startimg, (760, 570))
font = pygame.font.Font('freesansbold.ttf', 32) 


def showtext(textre, x, y, color = black, bgcolor = white, gameDisplay = gameDisplay):

    text = font.render(textre, True, color, bgcolor) 
    
    textRect = text.get_rect()  
     
    textRect.center = (x, y)

    gameDisplay.blit(text, textRect)


while start:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.KEYDOWN:
            start = False
          
        if event.type == pygame.MOUSEBUTTONDOWN:
            start = False
        
    gameDisplay.fill(white)
    gameDisplay.blit(startimg, (70, 0))
    showtext('Click Any Button On Mouse Or Keyboard To Continue', 450, 575)
    pygame.display.update()
    clock.tick(60)


bgimg = pygame.image.load('board.jpg')
bgimg = pygame.transform.scale(bgimg, (737, 623))

player = pygame.transform.scale(pygame.image.load('player.png'), (30, 40))
pl = pygame.transform.scale(pygame.image.load('player2.png'), (50, 40))

player1 = Player(player)
player2 = Player(pl, '+')
playing = player2

def main():
    gameDisplay = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Snakes And LaddeRs')
    black = (0,0,0)
    white = (255,255,255)
    clock = pygame.time.Clock()
    play = 1
    p = True
    while p:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed() == (1, 0, 0):
                    if (pygame.mouse.get_pos()[0] in range(315, 485)) & (pygame.mouse.get_pos()[1] in range(75, 125)):
                        p = False
                    elif (pygame.mouse.get_pos()[0] in range(315, 485)) & (pygame.mouse.get_pos()[1] in range(275, 325)):
                        play = 2
                        p = False
                    elif (pygame.mouse.get_pos()[0] in range(315, 485)) & (pygame.mouse.get_pos()[1] in range(475, 525)):
                        pygame.quit()
                        quit()

        gameDisplay.fill(white)
        showtext('One Player', 400, 100)
        showtext('Two Player', 400, 300)
        showtext('Quit Game', 400, 500)
        pygame.display.update()
        clock.tick(60)
    
    global player1
    global playing
    global player2
    player1 = Player(player)
    player2 = Player(pl, '+')
    playing = player1
    if play == 1:
        playing = player2
    gameDisplay = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Snakes And LaddeRs')
    black = (0,0,0)
    white = (255,255,255)
    start = True
    p = 0
    p2 = 0
    ch = 5
    k = 101
    dice = 0
    dic = 0
    playin = 0
    crashed = False
    rolled = False
    clock = pygame.time.Clock()
    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed() == (1, 0, 0):
                    if (pygame.mouse.get_pos()[0] in range(50, 150)) & (pygame.mouse.get_pos()[1] in range(350, 450)):
                        if (k > 10) | (rolled == False):
                            rolled = True
                            mep = dice
                            dic = dice
                            while dice == dic:
                                dic = roll_dice()
                            dice = dic
                            ch = dice
                            if playing == player1:
                                print(dice)
                                if mep == 5:
                                    if (play == 2)&(mep != 5):
                                        playing = player1
                                    if (p + dice + 1) > 100:
                                        p2 += 1
                                        p2 -= 1
                                    else:
                                        if play == 1 or playin == player1:
                                            p2 += dice + 1
                                        else:
                                            p += dice + 1
                                else:
                                    if (play == 2) & (mep != 5):
                                        playing = player2
                                    if (p2 + dice + 1) > 100:
                                        p += 1
                                        p -= 1
                                    else:
                                        if playin == player2:
                                            p += dice + 1
                                        p2 += dice + 1
                            else:
                                if mep == 5:
                                    if (play == 2) & (mep != 5):
                                        playing = player2
                                    if (p2 + dice + 1) > 100:
                                        p += 1
                                        p -= 1
                                    else:
                                        if playin == player2:
                                            p += dice + 1
                                        p2 += dice + 1
                                else:
                                    if (play == 2)&(mep != 5):
                                        playing = player1
                                    if (p + dice + 1) > 100:
                                        p2 += 1
                                        p2 -= 1
                                    else:
                                        if play == 1 or playin == player1:
                                            p2 += dice + 1
                                        else:
                                            p += dice + 1
                            k = 0


        gameDisplay.fill(white)
        gameDisplay.blit(bgimg, (0, 0))
        if not rolled:
            showtext('Roll Dice', 100, 400)
        else:
            gameDisplay.blit(dices[dice], (60, 360))
        
        if (p == 100 or p2 == 100) and playing.posin:
            for i in range(10):
                gameDisplay.fill(white)
                gameDisplay.blit(bgimg, (0, 0))
                gameDisplay.blit(dices[dice], (60, 360))
                playing.pblit(100, gameDisplay)
                showtext('Made By:', 100, 500)
                showtext('Rushi', 100, 550)
                time.sleep(0.05)
                pygame.display.update()
                clock.tick(60)
            break
        
        
        if dice == 5 & play == 2:
            if playing == player1:
                playing = player2
            elif playing == player2:
                playing =player1
        
        if playing == player1:
            k, p = playing.move(p, k, gameDisplay)
        else:
            k, p2 = playing.move(p2, k, gameDisplay)
        
        player2.pblit(player2.posin, gameDisplay)
        if play == 2:
            player1.pblit(player1.posin, gameDisplay)
        
        showtext('Made By:', 100, 500)
        showtext('Rushi', 100, 550)

        pygame.display.update()
        clock.tick(60)

    if crashed:
        main()
    else:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    main()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pressed() == (1, 0, 0):
                        if (pygame.mouse.get_pos()[0] in range(315, 485)) & (pygame.mouse.get_pos()[1] in range(275, 325)):
                            main()
                        elif (pygame.mouse.get_pos()[0] in range(315, 485)) & (pygame.mouse.get_pos()[1] in range(475, 525)):
                            pygame.quit()
                            quit()

            gameDisplay.fill(white)
            if playing == player1:
                showtext('Red Won', 400, 100)
            else:
                showtext('Blue Won', 400, 100)
            showtext('Play Again', 400, 300)
            showtext('Quit Game', 400, 500)
            pygame.display.update()
            clock.tick(60)

if __name__ == "__main__":
    main()
