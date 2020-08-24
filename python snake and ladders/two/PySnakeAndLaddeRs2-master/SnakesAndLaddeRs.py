# Made By Rushi
# Date : 7/22/2020
import pygame, time, random
from pygame.locals import *
from sys import exit as quit

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
poses = [
    ['26.6%', '89.5%'],
    ['32.3%', '89.5%'], ['38%', '89.5%'], ['43.7%', '89.5%'], ['49.4%', '89.5%'], ['55.1%', '89.5%'], ['60.8%', '89.5%'], ['66.5%', '89.5%'], ['72.2%', '89.5%'], ['77.9%', '89.5%'], ['83.6%', '89.5%'],
    ['83.6%', '80.5%'], ['77.9%', '80.5%'], ['72.2%', '80.5%'], ['66.5%', '80.5%'], ['60.8%', '80.5%'], ['55.1%', '80.5%'], ['49.4%', '80.5%'], ['43.7%', '80.5%'], ['38%', '80.5%'], ['32.3%', '80.5%'],
    ['32.3%', '71.5%'], ['38%', '71.5%'], ['43.7%', '71.5%'], ['49.4%', '71.5%'], ['55.1%', '71.5%'], ['60.8%', '71.5%'], ['66.5%', '71.5%'], ['72.2%', '71.5%'], ['77.9%', '71.5%'], ['83.6%', '71.5%'],
    ['83.6%', '62.5%'], ['77.9%', '62.5%'], ['72.2%', '62.5%'], ['66.5%', '62.5%'], ['60.8%', '62.5%'], ['55.1%', '62.5%'], ['49.4%', '62.5%'], ['43.7%', '62.5%'], ['38%', '62.5%'], ['32.3%', '62.5%'],
    ['32.3%', '53.5%'], ['38%', '53.5%'], ['43.7%', '53.5%'], ['49.4%', '53.5%'], ['55.1%', '53.5%'], ['60.8%', '53.5%'], ['66.5%', '53.5%'], ['72.2%', '53.5%'], ['77.9%', '53.5%'], ['83.6%', '53.5%'],
    ['83.6%', '44.5%'], ['77.9%', '44.5%'], ['72.2%', '44.5%'], ['66.5%', '44.5%'], ['60.8%', '44.5%'], ['55.1%', '44.5%'], ['49.4%', '44.5%'], ['43.7%', '44.5%'], ['38%', '44.5%'], ['32.3%', '44.5%'],
    ['32.3%', '35.5%'], ['38%', '35.5%'], ['43.7%', '35.5%'], ['49.4%', '35.5%'], ['55.1%', '35.5%'], ['60.8%', '35.5%'], ['66.5%', '35.5%'], ['72.2%', '35.5%'], ['77.9%', '35.5%'], ['83.6%', '35.5%'],
    ['83.6%', '26.5%'], ['77.9%', '26.5%'], ['72.2%', '26.5%'], ['66.5%', '26.5%'], ['60.8%', '26.5%'], ['55.1%', '26.5%'], ['49.4%', '26.5%'], ['43.7%', '26.5%'], ['38%', '26.5%'], ['32.3%', '26.5%'],
    ['32.3%', '17.5%'], ['38%', '17.5%'], ['43.7%', '17.5%'], ['49.4%', '17.5%'], ['55.1%', '17.5%'], ['60.8%', '17.5%'], ['66.5%', '17.5%'], ['72.2%', '17.5%'], ['77.9%', '17.5%'], ['83.6%', '17.5%'],
    ['83.6%', '8.5%'], ['77.9%', '8.5%'], ['72.2%', '8.5%'], ['66.5%', '8.5%'], ['60.8%', '8.5%'], ['55.1%', '8.5%'], ['49.4%', '8.5%'], ['43.7%', '8.5%'], ['38%', '8.5%'], ['32.3%', '8.5%']
]


def change(list):
    j = [0, 0]
    j[0] = float(list[0].split('%')[0]) * 8
    j[1] = float(list[1].split('%')[0]) * 6
    return tuple(j)


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
dices = [
    pygame.transform.scale(pygame.image.load('1.png'), (80, 80)),
    pygame.transform.scale(pygame.image.load('2.png'), (80, 80)),
    pygame.transform.scale(pygame.image.load('3.png'), (80, 80)),
    pygame.transform.scale(pygame.image.load('4.png'), (80, 80)),
    pygame.transform.scale(pygame.image.load('5.png'), (80, 80)),
    pygame.transform.scale(pygame.image.load('6.png'), (80, 80)),
]
player = pygame.transform.scale(pygame.image.load('player.png'), (30, 40))


def pblit(num, gameDisplay = gameDisplay):
    gameDisplay.blit(player, change(poses[num]))


rolled = False
crashed = False


def roll_dice():
    a = random.randrange(6)
    return a

ladpos = [
    [4, 56],
    [12, 50],
    [14, 55],
    [22, 58],
    [41, 79],
    [54, 88],
]
snakepos = [
    [28, 10],
    [37, 3],
    [47, 16],
    [75, 32],
    [94, 71],
    [96, 42],
]


def islad(pos):
    islad = False
    for i in ladpos:
        if i[0] == pos:
            islad = True
    return islad


def issnake(pos):
    issnake = False
    for i in snakepos:
        if i[0] == pos:
            issnake = True
    return issnake


def getnextlad(pos):
    if islad(pos):
        for i in ladpos:
            if i[0] == pos:
                pos = i[1]
    return pos


def getwheresnake(pos):
    if issnake(pos):
        for i in snakepos:
            if i[0] == pos:
                pos = i[1]
    return pos


def main():
    gameDisplay = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Snakes And LaddeRs')
    black = (0,0,0)
    white = (255,255,255)
    start = True
    pl = 0
    k = 101
    p = 0
    dice = 0
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
                            dic = dice
                            while dice == dic:
                                dic = roll_dice()
                            dice = dic
                            if (p + dice + 1) > 100:
                                p += 1
                                p -= 1
                            else:
                                p += dice + 1  
                            k = 0


        gameDisplay.fill(white)
        gameDisplay.blit(bgimg, (0, 0))
        if not rolled:
            showtext('Roll Dice', 100, 400)
        else:
            gameDisplay.blit(dices[dice], (60, 360))
        pblit(pl)
        if k < 10:
            time.sleep(0.00001)
            k += 1
        if (k == 10) & (pl < p):
            pl += 1
            k = 0
        elif (k == 10) & (pl == p):
            k = 1000
            pblit(getwheresnake(getnextlad(p)))
            pl = getwheresnake(getnextlad(p))
            p = pl
        if pl == 100:
            for i in range(25):
                gameDisplay.fill(white)
                gameDisplay.blit(bgimg, (0, 0))
                gameDisplay.blit(dices[dice], (60, 360))
                pblit(100)
                showtext('Made By:', 100, 500)
                showtext('Rushi', 100, 550)
                time.sleep(0.1)
                pygame.display.update()
                clock.tick(60)
            break
        
        showtext('Made By:', 100, 500)
        showtext('Rushi', 100, 550)

        pygame.display.update()
        clock.tick(60)

    if crashed:
        pygame.quit()
        quit()
    else:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pressed() == (1, 0, 0):
                        if (pygame.mouse.get_pos()[0] in range(315, 485)) & (pygame.mouse.get_pos()[1] in range(275, 325)):
                            main()
                        elif (pygame.mouse.get_pos()[0] in range(315, 485)) & (pygame.mouse.get_pos()[1] in range(475, 525)):
                            pygame.quit()
                            quit()

            gameDisplay.fill(white)
            showtext('Game Won', 400, 100)
            showtext('Play Again', 400, 300)
            showtext('Quit Game', 400, 500)
            pygame.display.update()
            clock.tick(60)

if __name__ == "__main__":
    main()
