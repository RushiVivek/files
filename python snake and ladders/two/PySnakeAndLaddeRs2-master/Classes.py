# Classes.py

import pygame,time,random
from pygame.locals import *

black = (0,0,0)
white = (255,255,255)

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

dices = [
    pygame.transform.scale(pygame.image.load('1.png'), (80, 80)),
    pygame.transform.scale(pygame.image.load('2.png'), (80, 80)),
    pygame.transform.scale(pygame.image.load('3.png'), (80, 80)),
    pygame.transform.scale(pygame.image.load('4.png'), (80, 80)),
    pygame.transform.scale(pygame.image.load('5.png'), (80, 80)),
    pygame.transform.scale(pygame.image.load('6.png'), (80, 80)),
]

def roll_dice():
    a = random.randrange(6)
    return a

class Player():
    
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
    
    def __init__(self, img, ko = 'hol'):
        self.ko = ko
        self.img = img
        self.poses = poses
        self.posin = 0
    
    def pos(self, posin):
        return self.poses[posin]
    
    def showtext(textre, x, y, gameDisplay, color = black, bgcolor = white):
        font = pygame.font.Font('freesansbold.ttf', 32) 
        text = font.render(textre, True, color, bgcolor)
        textRect = text.get_rect()  
        textRect.center = (x, y)
        gameDisplay.blit(text, textRect)
    
    def change(self, list):
        if self.ko == "hol":
            j = [0, 0]
            j[0] = float(list[0].split('%')[0]) * 8
            j[1] = float(list[1].split('%')[0]) * 6
            return tuple(j)
        else:
            j = [0, 0]
            j[0] = float(list[0].split('%')[0]) * 8-10
            j[1] = float(list[1].split('%')[0]) * 6
            return tuple(j)
    
    def islad(self, pos):
        islad = False
        for i in self.ladpos:
            if i[0] == pos:
                islad = True
        return islad
    
    def issnake(self, pos):
        issnake = False
        for i in self.snakepos:
            if i[0] == pos:
                issnake = True
        return issnake
    
    def getnextlad(self, pos):
        if self.islad(pos):
            for i in self.ladpos:
                if i[0] == pos:
                    pos = i[1]
        return pos
    
    def getwheresnake(self, pos):
        if self.issnake(pos):
            for i in self.snakepos:
                if i[0] == pos:
                    pos = i[1]
        return pos
    
    def pblit(self, num, gameDisplay):
        gameDisplay.blit(self.img, self.change(self.pos(num)))
    
    def move(self, posfin, k, gameDisplay):
        if k < 10:
            time.sleep(0.00001)
            k += 1
        if (k == 10) & (self.posin < posfin):
            self.posin += 1
            k = 0
        elif (k == 10) & (self.posin == posfin):
            k = 1000
            self.posin = self.getwheresnake(self.getnextlad(self.posin))
            self.pblit(self.posin, gameDisplay)
            posfin = self.posin
        return (k, posfin)
        