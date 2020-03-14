import os
import sys
import math
import pygame as pg
import pygame as pygame
import random
from tkinter import *
from tkinter import ttk
import pickle
from pygame.locals import *
file = 'Highscores.txt'
EmptyDict=[{'Name':'Empty',"Points":0,"Time":0}]
HSList = []
points = 0
point = str(points)
CAPTION = "ArchonDynasty: Shooting game."
SCREEN_SIZE = (1280, 720)
BACKGROUND = (0,0,0)
COLOR_KEY = (255, 0, 255)
BG = pg.image.load('background.png')
BG = pg.transform.scale(BG, SCREEN_SIZE)
SPIN_DICT = {pg.K_LEFT  :  1,
             pg.K_RIGHT : -1}

os.environ['SDL_VIDEO_CENTERED'] = '1'
pg.init()            
pg.display.set_caption(CAPTION)
pg.display.set_mode(SCREEN_SIZE)
TURRET1 = pg.image.load("turret1.png").convert_alpha()  
TURRET = pg.image.load("turret.png").convert_alpha()
Tutorial = False           

collisionList = [False, False, False, False,False, False, False, False,False, False, False, False,False, False, False, False]
Balllist1 = [920,random.randint(-280,1000)]
Balllist2 = [-200,random.randint(-280,1000)]
Balllist3 = [random.randint(-280,1000),920]
Balllist4 = [1340,random.randint(-280,1000)]
Balllist5 = [920,random.randint(-280,1000)]
Balllist6 = [-200,random.randint(-280,1000)]
Balllist7 = [random.randint(-280,1000),920]
Balllist8 = [1340,random.randint(-280,1000)]
Balllist9 = [920,random.randint(-280,1000)]
Balllist10 = [-200,random.randint(-280,1000)]
Balllist11 = [random.randint(-280,1000),920]
Balllist12 = [1340,random.randint(-280,1000)]
Balllist13 = [920,random.randint(-280,1000)]
Balllist14 = [-200,random.randint(-280,1000)]
Balllist15 = [random.randint(-280,1000),920]
Balllist16 = [1340,random.randint(-280,1000)]



a = 643
b = 385
a1 = 456
b1 = 865
a2 = 345
b2 = 456
health = 100
XL = []
YL = []
X1L = []
Y1L = []
X2L = []
Y2L = []
Angle1 = 90
print("Use the arrow keys to rotate the turret")
print("Use spacebar to shoot the balls")



Name = ""
Difficulty = 2


def ball1(Balllist1,collisionList,points,health,TURRET1):
    original_ball = TURRET1.subsurface((0,0,150,150))
    ball = original_ball.copy()
    surface = pg.display.get_surface()
    if collisionList[0]:
        c = random.randint(1,4)
        if c == 1:
            Balllist1[0] = random.randint(0,1280)
            Balllist1[1] = -200
        if c == 2:
            Balllist1[0] = random.randint(0,1280)
            Balllist1[1] = 920
        if c == 3:
            Balllist1[0] = -200
            Balllist1[1] = random.randint(-280,1000)
        if c == 4:
            Balllist1[0] = 1340
            Balllist1[1] = random.randint(-280,1000)
        points = points +20
        collisionList[0] = False
    if Balllist1[0] != 593:
        if Balllist1[0] >593:
            Balllist1[0] = Balllist1[0]-1
            surface.blit(ball, (Balllist1[0],Balllist1[1]))
            
        if Balllist1[0] <593:
            Balllist1[0] = Balllist1[0]+1
            surface.blit(ball, (Balllist1[0],Balllist1[1]))

    if Balllist1[1] != 267:                   
        if Balllist1[1] > 267:
            Balllist1[1] = Balllist1[1]-1
            surface.blit(ball, (Balllist1[0],Balllist1[1]))

        if Balllist1[1] < 267:
            Balllist1[1] = Balllist1[1]+1



    if Balllist1[0] in range(593-40, 593+40):
        if Balllist1[1] in range(267-40, 267+40):
            health=health - 10
            c = random.randint(1,4)
            if c == 1:
                Balllist1[0] = random.randint(0,1280)
                Balllist1[1] = -200
            if c == 2:
                Balllist1[0] = random.randint(0,1280)
                Balllist1[1] = 920
            if c == 3:
                Balllist1[0] = -200
                Balllist1[1] = random.randint(-280,1000)
            if c == 4:
                Balllist1[0] = 1340
                Balllist1[1] = random.randint(-280,1000)
    return points, health
def ball2(Balllist2,Collision1,points,health,TURRET1):
    original_ball = TURRET1.subsurface((0,0,150,150))
    ball = original_ball.copy()
    surface = pg.display.get_surface()
    if collisionList[1]:
        c = random.randint(1,4)
        if c == 1:
            Balllist2[0] = random.randint(0,1280)
            Balllist2[1] = -200
        if c == 2:
            Balllist2[0] = random.randint(0,1280)
            Balllist2[1] = 920
        if c == 3:
            Balllist2[0] = -200
            Balllist2[1] = random.randint(-280,1000)
        if c == 4:
            Balllist2[0] = 1340
            Balllist2[1] = random.randint(-280,1000)
        points = points +20
        collisionList[1] = False
    if Balllist2[0] != 593:
        if Balllist2[0] >593:
            Balllist2[0] = Balllist2[0]-1
            surface.blit(ball, (Balllist2[0],Balllist2[1]))            
        if Balllist2[0] <593:
            Balllist2[0] = Balllist2[0]+1
            surface.blit(ball, (Balllist2[0],Balllist2[1]))
    if Balllist2[1] != 267:                   
        if Balllist2[1] > 267:
           Balllist2[1] = Balllist2[1]-1
           surface.blit(ball, (Balllist2[0],Balllist2[1]))
        if Balllist2[1] < 267:
            Balllist2[1] = Balllist2[1]+1
            surface.blit(ball, (Balllist2[0],Balllist2[1]))


    if Balllist2[0] in range(593-40, 593+40):
        if Balllist2[1] in range(267-40, 267+40):
            health=health - 10
            c = random.randint(1,4)
            if c == 1:
                Balllist2[0] = random.randint(0,1280)
                Balllist2[1] = -200
            if c == 2:
                Balllist2[0] = random.randint(0,1280)
                Balllist2[1] = 920
            if c == 3:
                Balllist2[0] = -200
                Balllist2[1] = random.randint(-280,1000)
            if c == 4:
                Balllist2[0] = 1340
                Balllist2[1] = random.randint(-280,1000)
    return points, health
def ball3(Balllist3,Collision2,points,health,TURRET1):
    original_ball = TURRET1.subsurface((0,0,150,150))
    ball = original_ball.copy()
    surface = pg.display.get_surface()
    if collisionList[2]:
        c = random.randint(1,4)
        if c == 1:
            Balllist3[0] = random.randint(0,1280)
            Balllist3[1] = -200
        if c == 2:
            ###Movement for balls toward the centre of the screen
            Balllist3[0] = random.randint(0,1280)
            Balllist3[1] = 920
        if c == 3:
            Balllist3[0] = -200
            Balllist3[1] = random.randint(-280,1000)
        if c == 4:
            Balllist3[0] = 1340
            Balllist3[1] = random.randint(-280,1000)
        points = points + 20
        collisionList[2] = False
    if Balllist3[0] != 593:
        if Balllist3[0] >593:
            Balllist3[0] = Balllist3[0]-1
            surface.blit(ball, (Balllist3[0],Balllist3[1]))

            
        if Balllist3[0] <593:
            Balllist3[0] = Balllist3[0]+1
            surface.blit(ball, (Balllist3[0],Balllist3[1]))

    if Balllist3[1] != 267:                   
        if Balllist3[1] > 267:
            Balllist3[1] = Balllist3[1]-1
            surface.blit(ball, (Balllist3[0],Balllist3[1]))

        if Balllist3[1] < 267:
            Balllist3[1] = Balllist3[1]+1
            surface.blit(ball, (Balllist3[0],Balllist3[1]))

    if Balllist3[0] in range(593-40, 593+40):
        if Balllist3[1] in range(267-40, 267+40):
            health = health - 10
            c = random.randint(1,4)
            if c == 1:
                Balllist3[0] = random.randint(0,1280)
                Balllist3[1] = -200
            if c == 2:
                Balllist3[0] = random.randint(0,1280)
                Balllist3[1] = 920
            if c == 3:
                Balllist3[0] = -200
                Balllist3[1] = random.randint(-280,1000)
            if c == 4:
                Balllist3[0] = 1340
                Balllist3[1] = random.randint(-280,1000)
                
    return points, health

def ball4(Balllist4,Collision2,points,health,TURRET1):
    original_ball = TURRET1.subsurface((0,0,150,150))
    ball = original_ball.copy()
    surface = pg.display.get_surface()
    if collisionList[3]:
        c = random.randint(1,4)
        if c == 1:
            Balllist4[0] = random.randint(0,1280)
            Balllist4[1] = -200
        if c == 2:
            ###Movement for balls toward the centre of the screen
            Balllist4[0] = random.randint(0,1280)
            Balllist4[1] = 920
        if c == 3:
            Balllist4[0] = -200
            Balllist4[1] = random.randint(-280,1000)
        if c == 4:
            Balllist4[0] = 1340
            Balllist4[1] = random.randint(-280,1000)
        points = points + 20
        collisionList[3] = False
    if Balllist4[0] != 593:
        if Balllist4[0] >593:
            Balllist4[0] = Balllist4[0]-1
            surface.blit(ball, (Balllist4[0],Balllist4[1]))

            
        if Balllist4[0] <593:
            Balllist4[0] = Balllist4[0]+1
            surface.blit(ball, (Balllist4[0],Balllist4[1]))

    if Balllist4[1] != 267:                   
        if Balllist4[1] > 267:
            Balllist4[1] = Balllist4[1]-1
            surface.blit(ball, (Balllist4[0],Balllist4[1]))

        if Balllist4[1] < 267:
            Balllist4[1] = Balllist4[1]+1
            surface.blit(ball, (Balllist4[0],Balllist4[1]))

    if Balllist4[0] in range(593-40, 593+40):
        if Balllist4[1] in range(267-40, 267+40):
            health = health - 10
            c = random.randint(1,4)
            if c == 1:
                Balllist4[0] = random.randint(0,1280)
                Balllist4[1] = -200
            if c == 2:
                Balllist4[0] = random.randint(0,1280)
                Balllist4[1] = 920
            if c == 3:
                Balllist4[0] = -200
                Balllist4[1] = random.randint(-280,1000)
            if c == 4:
                Balllist4[0] = 1340
                Balllist4[1] = random.randint(-280,1000)
                
    return points, health

def ball5(Balllist5,collisionList,points,health,TURRET1):
    original_ball = TURRET1.subsurface((0,0,150,150))
    ball = original_ball.copy()
    surface = pg.display.get_surface()
    if collisionList[4]:
        c = random.randint(1,4)
        if c == 1:
            Balllist5[0] = random.randint(0,1280)
            Balllist5[1] = -200
        if c == 2:
            Balllist5[0] = random.randint(0,1280)
            Balllist5[1] = 920
        if c == 3:
            Balllist5[0] = -200
            Balllist5[1] = random.randint(-280,1000)
        if c == 4:
            Balllist5[0] = 1340
            Balllist5[1] = random.randint(-280,1000)
        points = points +20
        collisionList[4] = False
    if Balllist5[0] != 593:
        if Balllist5[0] >593:
            Balllist5[0] = Balllist5[0]-1
            surface.blit(ball, (Balllist5[0],Balllist5[1]))
            
        if Balllist5[0] <593:
            Balllist5[0] = Balllist5[0]+1
            surface.blit(ball, (Balllist5[0],Balllist5[1]))

    if Balllist5[1] != 267:                   
        if Balllist5[1] > 267:
            Balllist5[1] = Balllist5[1]-1
            surface.blit(ball, (Balllist5[0],Balllist5[1]))

        if Balllist5[1] < 267:
            Balllist5[1] = Balllist5[1]+1



    if Balllist5[0] in range(593-40, 593+40):
        if Balllist5[1] in range(267-40, 267+40):
            health=health - 10
            c = random.randint(1,4)
            if c == 1:
                Balllist5[0] = random.randint(0,1280)
                Balllist5[1] = -200
            if c == 2:
                Balllist5[0] = random.randint(0,1280)
                Balllist5[1] = 920
            if c == 3:
                Balllist5[0] = -200
                Balllist5[1] = random.randint(-280,1000)
            if c == 4:
                Balllist5[0] = 1340
                Balllist5[1] = random.randint(-280,1000)
    return points, health
def ball6(Balllist6,Collision1,points,health,TURRET1):
    original_ball = TURRET1.subsurface((0,0,150,150))
    ball = original_ball.copy()
    surface = pg.display.get_surface()
    if collisionList[5]:
        c = random.randint(1,4)
        if c == 1:
            Balllist6[0] = random.randint(0,1280)
            Balllist6[1] = -200
        if c == 2:
            Balllist6[0] = random.randint(0,1280)
            Balllist6[1] = 920
        if c == 3:
            Balllist6[0] = -200
            Balllist6[1] = random.randint(-280,1000)
        if c == 4:
            Balllist6[0] = 1340
            Balllist6[1] = random.randint(-280,1000)
        points = points +20
        collisionList[5] = False
    if Balllist6[0] != 593:
        if Balllist6[0] >593:
            Balllist6[0] = Balllist6[0]-1
            surface.blit(ball, (Balllist6[0],Balllist6[1]))            
        if Balllist6[0] <593:
            Balllist6[0] = Balllist6[0]+1
            surface.blit(ball, (Balllist6[0],Balllist6[1]))
    if Balllist6[1] != 267:                   
        if Balllist6[1] > 267:
           Balllist6[1] = Balllist6[1]-1
           surface.blit(ball, (Balllist6[0],Balllist6[1]))
        if Balllist6[1] < 267:
            Balllist6[1] = Balllist6[1]+1
            surface.blit(ball, (Balllist6[0],Balllist6[1]))


    if Balllist6[0] in range(593-40, 593+40):
        if Balllist6[1] in range(267-40, 267+40):
            health=health - 10
            c = random.randint(1,4)
            if c == 1:
                Balllist6[0] = random.randint(0,1280)
                Balllist6[1] = -200
            if c == 2:
                Balllist6[0] = random.randint(0,1280)
                Balllist6[1] = 920
            if c == 3:
                Balllist6[0] = -200
                Balllist6[1] = random.randint(-280,1000)
            if c == 4:
                Balllist6[0] = 1340
                Balllist6[1] = random.randint(-280,1000)
    return points, health
def ball7(Balllist7,Collision2,points,health,TURRET1):
    original_ball = TURRET1.subsurface((0,0,150,150))
    ball = original_ball.copy()
    surface = pg.display.get_surface()
    if collisionList[6]:
        c = random.randint(1,4)
        if c == 1:
            Balllist7[0] = random.randint(0,1280)
            Balllist7[1] = -200
        if c == 2:
            ###Movement for balls toward the centre of the screen
            Balllist7[0] = random.randint(0,1280)
            Balllist7[1] = 920
        if c == 3:
            Balllist7[0] = -200
            Balllist7[1] = random.randint(-280,1000)
        if c == 4:
            Balllist7[0] = 1340
            Balllist7[1] = random.randint(-280,1000)
        points = points + 20
        collisionList[6] = False
    if Balllist7[0] != 593:
        if Balllist7[0] >593:
            Balllist7[0] = Balllist7[0]-1
            surface.blit(ball, (Balllist7[0],Balllist7[1]))

            
        if Balllist7[0] <593:
            Balllist7[0] = Balllist7[0]+1
            surface.blit(ball, (Balllist7[0],Balllist7[1]))

    if Balllist7[1] != 267:                   
        if Balllist7[1] > 267:
            Balllist7[1] = Balllist7[1]-1
            surface.blit(ball, (Balllist7[0],Balllist7[1]))

        if Balllist7[1] < 267:
            Balllist7[1] = Balllist7[1]+1
            surface.blit(ball, (Balllist7[0],Balllist7[1]))

    if Balllist7[0] in range(593-40, 593+40):
        if Balllist7[1] in range(267-40, 267+40):
            health = health - 10
            c = random.randint(1,4)
            if c == 1:
                Balllist7[0] = random.randint(0,1280)
                Balllist7[1] = -200
            if c == 2:
                Balllist7[0] = random.randint(0,1280)
                Balllist7[1] = 920
            if c == 3:
                Balllist7[0] = -200
                Balllist7[1] = random.randint(-280,1000)
            if c == 4:
                Balllist7[0] = 1340
                Balllist7[1] = random.randint(-280,1000)
                
    return points, health

def ball8(Balllist8,Collision2,points,health,TURRET1):
    original_ball = TURRET1.subsurface((0,0,150,150))
    ball = original_ball.copy()
    surface = pg.display.get_surface()
    if collisionList[7]:
        c = random.randint(1,4)
        if c == 1:
            Balllist8[0] = random.randint(0,1280)
            Balllist8[1] = -200
        if c == 2:
            ###Movement for balls toward the centre of the screen
            Balllist8[0] = random.randint(0,1280)
            Balllist8[1] = 920
        if c == 3:
            Balllist8[0] = -200
            Balllist8[1] = random.randint(-280,1000)
        if c == 4:
            Balllist8[0] = 1340
            Balllist8[1] = random.randint(-280,1000)
        points = points + 20
        collisionList[7] = False
    if Balllist8[0] != 593:
        if Balllist8[0] >593:
            Balllist8[0] = Balllist8[0]-1
            surface.blit(ball, (Balllist8[0],Balllist8[1]))

            
        if Balllist8[0] <593:
            Balllist8[0] = Balllist8[0]+1
            surface.blit(ball, (Balllist8[0],Balllist8[1]))

    if Balllist8[1] != 267:                   
        if Balllist8[1] > 267:
            Balllist8[1] = Balllist8[1]-1
            surface.blit(ball, (Balllist8[0],Balllist8[1]))

        if Balllist8[1] < 267:
            Balllist8[1] = Balllist8[1]+1
            surface.blit(ball, (Balllist8[0],Balllist8[1]))

    if Balllist8[0] in range(593-40, 593+40):
        if Balllist8[1] in range(267-40, 267+40):
            health = health - 10
            c = random.randint(1,4)
            if c == 1:
                Balllist8[0] = random.randint(0,1280)
                Balllist8[1] = -200
            if c == 2:
                Balllist8[0] = random.randint(0,1280)
                Balllist8[1] = 920
            if c == 3:
                Balllist8[0] = -200
                Balllist8[1] = random.randint(-280,1000)
            if c == 4:
                Balllist8[0] = 1340
                Balllist8[1] = random.randint(-280,1000)
                
    return points, health
                    

def ball9(Balllist9,collisionList,points,health,TURRET1):
    original_ball = TURRET1.subsurface((0,0,150,150))
    ball = original_ball.copy()
    surface = pg.display.get_surface()
    if collisionList[8]:
        c = random.randint(1,4)
        if c == 1:
            Balllist9[0] = random.randint(0,1280)
            Balllist9[1] = -200
        if c == 2:
            Balllist9[0] = random.randint(0,1280)
            Balllist9[1] = 920
        if c == 3:
            Balllist9[0] = -200
            Balllist9[1] = random.randint(-280,1000)
        if c == 4:
            Balllist9[0] = 1340
            Balllist9[1] = random.randint(-280,1000)
        points = points +20
        collisionList[8] = False
    if Balllist9[0] != 593:
        if Balllist9[0] >593:
            Balllist9[0] = Balllist9[0]-1
            surface.blit(ball, (Balllist9[0],Balllist9[1]))
            
        if Balllist9[0] <593:
            Balllist9[0] = Balllist9[0]+1
            surface.blit(ball, (Balllist9[0],Balllist9[1]))

    if Balllist9[1] != 267:                   
        if Balllist9[1] > 267:
            Balllist9[1] = Balllist9[1]-1
            surface.blit(ball, (Balllist9[0],Balllist9[1]))

        if Balllist9[1] < 267:
            Balllist9[1] = Balllist9[1]+1



    if Balllist9[0] in range(593-40, 593+40):
        if Balllist9[1] in range(267-40, 267+40):
            health=health - 10
            c = random.randint(1,4)
            if c == 1:
                Balllist9[0] = random.randint(0,1280)
                Balllist9[1] = -200
            if c == 2:
                Balllist9[0] = random.randint(0,1280)
                Balllist9[1] = 920
            if c == 3:
                Balllist9[0] = -200
                Balllist9[1] = random.randint(-280,1000)
            if c == 4:
                Balllist9[0] = 1340
                Balllist9[1] = random.randint(-280,1000)
    return points, health
def ball10(Balllist10,Collision1,points,health,TURRET1):
    original_ball = TURRET1.subsurface((0,0,150,150))
    ball = original_ball.copy()
    surface = pg.display.get_surface()
    if collisionList[9]:
        c = random.randint(1,4)
        if c == 1:
            Balllist10[0] = random.randint(0,1280)
            Balllist10[1] = -200
        if c == 2:
            Balllist10[0] = random.randint(0,1280)
            Balllist10[1] = 920
        if c == 3:
            Balllist10[0] = -200
            Balllist10[1] = random.randint(-280,1000)
        if c == 4:
            Balllist10[0] = 1340
            Balllist10[1] = random.randint(-280,1000)
        points = points +20
        collisionList[9] = False
    if Balllist10[0] != 593:
        if Balllist10[0] >593:
            Balllist10[0] = Balllist10[0]-1
            surface.blit(ball, (Balllist10[0],Balllist10[1]))            
        if Balllist10[0] <593:
            Balllist10[0] = Balllist10[0]+1
            surface.blit(ball, (Balllist10[0],Balllist10[1]))
    if Balllist10[1] != 267:                   
        if Balllist10[1] > 267:
           Balllist10[1] = Balllist10[1]-1
           surface.blit(ball, (Balllist10[0],Balllist10[1]))
        if Balllist10[1] < 267:
            Balllist10[1] = Balllist10[1]+1
            surface.blit(ball, (Balllist10[0],Balllist10[1]))


    if Balllist10[0] in range(593-40, 593+40):
        if Balllist10[1] in range(267-40, 267+40):
            health=health - 10
            c = random.randint(1,4)
            if c == 1:
                Balllist10[0] = random.randint(0,1280)
                Balllist10[1] = -200
            if c == 2:
                Balllist10[0] = random.randint(0,1280)
                Balllist10[1] = 920
            if c == 3:
                Balllist10[0] = -200
                Balllist10[1] = random.randint(-280,1000)
            if c == 4:
                Balllist10[0] = 1340
                Balllist10[1] = random.randint(-280,1000)
    return points, health
def ball11(Balllist11,Collision2,points,health,TURRET1):
    original_ball = TURRET1.subsurface((0,0,150,150))
    ball = original_ball.copy()
    surface = pg.display.get_surface()
    if collisionList[10]:
        c = random.randint(1,4)
        if c == 1:
            Balllist11[0] = random.randint(0,1280)
            Balllist11[1] = -200
        if c == 2:
            ###Movement for balls toward the centre of the screen
            Balllist11[0] = random.randint(0,1280)
            Balllist11[1] = 920
        if c == 3:
            Balllist11[0] = -200
            Balllist11[1] = random.randint(-280,1000)
        if c == 4:
            Balllist11[0] = 1340
            Balllist11[1] = random.randint(-280,1000)
        points = points + 20
        collisionList[10] = False
    if Balllist11[0] != 593:
        if Balllist11[0] >593:
            Balllist11[0] = Balllist11[0]-1
            surface.blit(ball, (Balllist11[0],Balllist11[1]))

            
        if Balllist11[0] <593:
            Balllist11[0] = Balllist11[0]+1
            surface.blit(ball, (Balllist11[0],Balllist11[1]))

    if Balllist11[1] != 267:                   
        if Balllist11[1] > 267:
            Balllist11[1] = Balllist11[1]-1
            surface.blit(ball, (Balllist11[0],Balllist11[1]))

        if Balllist11[1] < 267:
            Balllist11[1] = Balllist11[1]+1
            surface.blit(ball, (Balllist11[0],Balllist11[1]))

    if Balllist11[0] in range(593-40, 593+40):
        if Balllist11[1] in range(267-40, 267+40):
            health = health - 10
            c = random.randint(1,4)
            if c == 1:
                Balllist11[0] = random.randint(0,1280)
                Balllist11[1] = -200
            if c == 2:
                Balllist11[0] = random.randint(0,1280)
                Balllist11[1] = 920
            if c == 3:
                Balllist11[0] = -200
                Balllist11[1] = random.randint(-280,1000)
            if c == 4:
                Balllist11[0] = 1340
                Balllist11[1] = random.randint(-280,1000)
                
    return points, health

def ball12(Balllist12,Collision2,points,health,TURRET1):
    original_ball = TURRET1.subsurface((0,0,150,150))
    ball = original_ball.copy()
    surface = pg.display.get_surface()
    if collisionList[11]:
        c = random.randint(1,4)
        if c == 1:
            Balllist12[0] = random.randint(0,1280)
            Balllist12[1] = -200
        if c == 2:
            ###Movement for balls toward the centre of the screen
            Balllist12[0] = random.randint(0,1280)
            Balllist12[1] = 920
        if c == 3:
            Balllist12[0] = -200
            Balllist12[1] = random.randint(-280,1000)
        if c == 4:
            Balllist12[0] = 1340
            Balllist12[1] = random.randint(-280,1000)
        points = points + 20
        collisionList[11] = False
    if Balllist12[0] != 593:
        if Balllist12[0] >593:
            Balllist12[0] = Balllist12[0]-1
            surface.blit(ball, (Balllist12[0],Balllist12[1]))

            
        if Balllist12[0] <593:
            Balllist12[0] = Balllist12[0]+1
            surface.blit(ball, (Balllist12[0],Balllist12[1]))

    if Balllist12[1] != 267:                   
        if Balllist12[1] > 267:
            Balllist12[1] = Balllist12[1]-1
            surface.blit(ball, (Balllist12[0],Balllist12[1]))

        if Balllist12[1] < 267:
            Balllist12[1] = Balllist12[1]+1
            surface.blit(ball, (Balllist12[0],Balllist12[1]))

    if Balllist12[0] in range(593-40, 593+40):
        if Balllist12[1] in range(267-40, 267+40):
            health = health - 10
            c = random.randint(1,4)
            if c == 1:
                Balllist12[0] = random.randint(0,1280)
                Balllist12[1] = -200
            if c == 2:
                Balllist12[0] = random.randint(0,1280)
                Balllist12[1] = 920
            if c == 3:
                Balllist12[0] = -200
                Balllist12[1] = random.randint(-280,1000)
            if c == 4:
                Balllist12[0] = 1340
                Balllist12[1] = random.randint(-280,1000)
                
    return points, health

def ball13(Balllist13,collisionList,points,health,TURRET1):
    original_ball = TURRET1.subsurface((0,0,150,150))
    ball = original_ball.copy()
    surface = pg.display.get_surface()
    if collisionList[12]:
        c = random.randint(1,4)
        if c == 1:
            Balllist13[0] = random.randint(0,1280)
            Balllist13[1] = -200
        if c == 2:
            Balllist13[0] = random.randint(0,1280)
            Balllist13[1] = 920
        if c == 3:
            Balllist13[0] = -200
            Balllist13[1] = random.randint(-280,1000)
        if c == 4:
            Balllist13[0] = 1340
            Balllist13[1] = random.randint(-280,1000)
        points = points +20
        collisionList[12] = False
    if Balllist13[0] != 593:
        if Balllist13[0] >593:
            Balllist13[0] = Balllist13[0]-1
            surface.blit(ball, (Balllist13[0],Balllist13[1]))
            
        if Balllist13[0] <593:
            Balllist13[0] = Balllist13[0]+1
            surface.blit(ball, (Balllist13[0],Balllist13[1]))

    if Balllist13[1] != 267:                   
        if Balllist13[1] > 267:
            Balllist13[1] = Balllist13[1]-1
            surface.blit(ball, (Balllist13[0],Balllist13[1]))

        if Balllist13[1] < 267:
            Balllist13[1] = Balllist13[1]+1



    if Balllist13[0] in range(593-40, 593+40):
        if Balllist13[1] in range(267-40, 267+40):
            health=health - 10
            c = random.randint(1,4)
            if c == 1:
                Balllist13[0] = random.randint(0,1280)
                Balllist13[1] = -200
            if c == 2:
                Balllist13[0] = random.randint(0,1280)
                Balllist13[1] = 920
            if c == 3:
                Balllist13[0] = -200
                Balllist13[1] = random.randint(-280,1000)
            if c == 4:
                Balllist13[0] = 1340
                Balllist13[1] = random.randint(-280,1000)
    return points, health
def ball14(Balllist14,Collision1,points,health,TURRET1):
    original_ball = TURRET1.subsurface((0,0,150,150))
    ball = original_ball.copy()
    surface = pg.display.get_surface()
    if collisionList[13]:
        c = random.randint(1,4)
        if c == 1:
            Balllist14[0] = random.randint(0,1280)
            Balllist14[1] = -200
        if c == 2:
            Balllist14[0] = random.randint(0,1280)
            Balllist14[1] = 920
        if c == 3:
            Balllist14[0] = -200
            Balllist14[1] = random.randint(-280,1000)
        if c == 4:
            Balllist14[0] = 1340
            Balllist14[1] = random.randint(-280,1000)
        points = points +20
        collisionList[13] = False
    if Balllist14[0] != 593:
        if Balllist14[0] >593:
            Balllist14[0] = Balllist14[0]-1
            surface.blit(ball, (Balllist14[0],Balllist14[1]))            
        if Balllist14[0] <593:
            Balllist14[0] = Balllist14[0]+1
            surface.blit(ball, (Balllist14[0],Balllist14[1]))
    if Balllist14[1] != 267:                   
        if Balllist14[1] > 267:
           Balllist14[1] = Balllist14[1]-1
           surface.blit(ball, (Balllist14[0],Balllist14[1]))
        if Balllist14[1] < 267:
            Balllist14[1] = Balllist14[1]+1
            surface.blit(ball, (Balllist14[0],Balllist14[1]))


    if Balllist14[0] in range(593-40, 593+40):
        if Balllist14[1] in range(267-40, 267+40):
            health=health - 10
            c = random.randint(1,4)
            if c == 1:
                Balllist14[0] = random.randint(0,1280)
                Balllist14[1] = -200
            if c == 2:
                Balllist14[0] = random.randint(0,1280)
                Balllist14[1] = 920
            if c == 3:
                Balllist14[0] = -200
                Balllist14[1] = random.randint(-280,1000)
            if c == 4:
                Balllist14[0] = 1340
                Balllist14[1] = random.randint(-280,1000)
    return points, health
def ball15(Balllist15,Collision2,points,health,TURRET1):
    original_ball = TURRET1.subsurface((0,0,150,150))
    ball = original_ball.copy()
    surface = pg.display.get_surface()
    if collisionList[14]:
        c = random.randint(1,4)
        if c == 1:
            Balllist15[0] = random.randint(0,1280)
            Balllist15[1] = -200
        if c == 2:
            ###Movement for balls toward the centre of the screen
            Balllist15[0] = random.randint(0,1280)
            Balllist15[1] = 920
        if c == 3:
            Balllist15[0] = -200
            Balllist15[1] = random.randint(-280,1000)
        if c == 4:
            Balllist15[0] = 1340
            Balllist15[1] = random.randint(-280,1000)
        points = points + 20
        collisionList[14] = False
    if Balllist15[0] != 593:
        if Balllist15[0] >593:
            Balllist15[0] = Balllist15[0]-1
            surface.blit(ball, (Balllist15[0],Balllist15[1]))

            
        if Balllist15[0] <593:
            Balllist15[0] = Balllist15[0]+1
            surface.blit(ball, (Balllist15[0],Balllist15[1]))

    if Balllist15[1] != 267:                   
        if Balllist15[1] > 267:
            Balllist15[1] = Balllist15[1]-1
            surface.blit(ball, (Balllist15[0],Balllist15[1]))

        if Balllist15[1] < 267:
            Balllist15[1] = Balllist15[1]+1
            surface.blit(ball, (Balllist15[0],Balllist15[1]))

    if Balllist15[0] in range(593-40, 593+40):
        if Balllist15[1] in range(267-40, 267+40):
            health = health - 10
            c = random.randint(1,4)
            if c == 1:
                Balllist15[0] = random.randint(0,1280)
                Balllist15[1] = -200
            if c == 2:
                Balllist15[0] = random.randint(0,1280)
                Balllist15[1] = 920
            if c == 3:
                Balllist15[0] = -200
                Balllist15[1] = random.randint(-280,1000)
            if c == 4:
                Balllist15[0] = 1340
                Balllist15[1] = random.randint(-280,1000)
                
    return points, health

def ball16(Balllist16,Collision2,points,health,TURRET1):
    original_ball = TURRET1.subsurface((0,0,150,150))
    ball = original_ball.copy()
    surface = pg.display.get_surface()
    if collisionList[15]:
        c = random.randint(1,4)
        if c == 1:
            Balllist16[0] = random.randint(0,1280)
            Balllist16[1] = -200
        if c == 2:
            ###Movement for balls toward the centre of the screen
            Balllist16[0] = random.randint(0,1280)
            Balllist16[1] = 920
        if c == 3:
            Balllist16[0] = -200
            Balllist16[1] = random.randint(-280,1000)
        if c == 4:
            Balllist16[0] = 1340
            Balllist16[1] = random.randint(-280,1000)
        points = points + 20
        collisionList[15] = False
    if Balllist16[0] != 593:
        if Balllist16[0] >593:
            Balllist16[0] = Balllist16[0]-1
            surface.blit(ball, (Balllist16[0],Balllist16[1]))

            
        if Balllist16[0] <593:
            Balllist16[0] = Balllist16[0]+1
            surface.blit(ball, (Balllist16[0],Balllist16[1]))

    if Balllist16[1] != 267:                   
        if Balllist16[1] > 267:
            Balllist16[1] = Balllist16[1]-1
            surface.blit(ball, (Balllist16[0],Balllist16[1]))

        if Balllist16[1] < 267:
            Balllist16[1] = Balllist16[1]+1
            surface.blit(ball, (Balllist16[0],Balllist16[1]))

    if Balllist16[0] in range(593-40, 593+40):
        if Balllist16[1] in range(267-40, 267+40):
            health = health - 10
            c = random.randint(1,4)
            if c == 1:
                Balllist16[0] = random.randint(0,1280)
                Balllist16[1] = -200
            if c == 2:
                Balllist16[0] = random.randint(0,1280)
                Balllist16[1] = 920
            if c == 3:
                Balllist16[0] = -200
                Balllist16[1] = random.randint(-280,1000)
            if c == 4:
                Balllist16[0] = 1340
                Balllist16[1] = random.randint(-280,1000)
                
    return points, health
                    

                    
                    
def GameOver(Name,points,file,Timer):
    Name = Name.get()
    print(Name)
    #Game over, write name and points to highscores file
    namepoints = {'Name': Name, 'Points': points, 'Time': Timer}
    with open (file, 'rb') as file_handler:
        HSList = pickle.load(file_handler)
    HSList.append(namepoints)
    with open(file,'wb') as file_handler:
        pickle.dump((HSList),(file_handler))
    pg.display.quit()
    #Open the python GUI for highscores
    
    import HighscoresDisplay
    sys.exit()
with open ('angle.txt', 'wb') as file_handler: #Create text file for the angle to go in
    pickle.dump((Angle1),(file_handler))
###Name Check to 5 char

###
#####Test for the file, if file doesn't exist write empty to file on user command
def Continue(root):
    print("Scores will not be saved for this game")
    root.withdraw()
def ResetScores(root, file):
    with open(file,'wb') as file_handler:
        pickle.dump((EmptyDict),(file_handler))
    root.quit()
    root.withdraw()

    
def HighscoresGUIError():
    root = Tk()
    root.geometry('1280x720')
    root.title("Warning")
    TextA = "Warning, your score will not be saved for this game"
    TextB = "please chose one of the options below"
    ttk.Label(root, text = TextA, font = (TextA,40)).grid(column=0,row=0)
    ttk.Label(root, text = TextB, font = (TextB,40)).grid(column=0,row=1)
    ttk.Button(root, text = "Reset highscores to allow future highscore to be saved", command=lambda: ResetScores(root, file)).grid(column=0,row=2)
    ttk.Button(root, text = "Continue without saving", command=lambda: Continue(root)).grid(column=0,row=3)
    root.mainloop()
#####

try:
    with open(file,"rb")as file_handler:
        custOut = pickle.load(file_handler)
except FileNotFoundError:
    HighscoresGUIError()    
class Turret(object): 
    def __init__(self, location):
        self.original_barrel = TURRET.subsurface((0,0,150,150))
        self.barrel = self.original_barrel.copy()
        self.rect = self.barrel.get_rect(center=(640,320))
        self.angle = 90
        self.spin = 0
        self.rotate_speed = 3
        self.rotate(True)
    def rotate(self, force=False):
        if self.spin or force:
            #Get angle from file, get new angle, write to file
            with open ('angle.txt', 'rb') as file_handler:
                self.angle = pickle.load(file_handler)
            self.angle += self.rotate_speed*self.spin
            with open ('angle.txt', 'wb') as file_handler:
                pickle.dump((self.angle),(file_handler))
            
            self.barrel = pg.transform.rotate(self.original_barrel, (self.angle))
            self.rect = self.barrel.get_rect(center=self.rect.center)

    def get_event(self, event, objects):
        if event.type == pg.KEYDOWN: #Shooting a bullet keypress
            if event.key == pg.K_SPACE:
                objects.add(Laser(self.rect.center, self.angle))


    def update(self, keys):
        self.spin = 0
        for key in SPIN_DICT: #Get keypress for rotation of
            if keys[key]:
                self.spin += SPIN_DICT[key]
                self.rotate()

    def draw(self, surface):

        surface.blit(BG,(0,0))
        surface.blit(self.barrel, self.rect)
        
class Laser(pg.sprite.Sprite):
    def __init__(self, location, angle):
        pg.sprite.Sprite.__init__(self)
        self.original_laser = TURRET.subsurface((150,0,150,150))
        self.angle = -math.radians(angle-135)
        self.image = pg.transform.rotate(self.original_laser, angle)
        self.rect = self.image.get_rect(center=location)
        self.move = [self.rect.x, self.rect.y]
        self.speed_magnitude = 5
        self.speed = (self.speed_magnitude*math.cos(self.angle),
                      self.speed_magnitude*math.sin((self.angle)))
        self.done = False


    def update(self, screen_rect,collisionList,points,point, health,Name,HsList,Balllist1,Balllist2,Balllist3,Balllist4,Balllist5,Balllist6,Balllist7,Balllist8,Balllist9,Balllist10,Balllist11,Balllist12,Balllist13,Balllist14,Balllist15,Balllist16):
        self.move[0] += self.speed[0]
        self.move[1] += self.speed[1]
        self.rect.topleft = self.move
        self.remove(screen_rect,collisionList,points,point,health,Name,HsList,Balllist1,Balllist2,Balllist3,Balllist4,Balllist5,Balllist6,Balllist7,Balllist8,Balllist9,Balllist10,Balllist11,Balllist12,Balllist13,Balllist14,Balllist15,Balllist16)


    def remove(self, screen_rect,collisionList,points,point,health,Name,HSList,Balllist1,Balllist2,Balllist3,Balllist4,Balllist5,Balllist6,Balllist7,Balllist8,Balllist9,Balllist10,Balllist11,Balllist12,Balllist13,Balllist14,Balllist15,Balllist16):
        if self.rect[0] in range(Balllist1[0]-60,Balllist1[0]) and self.rect[1] in range(Balllist1[1]-60,Balllist1[1]):
            self.kill()
            collisionList[0] = True          
        if self.rect[0] in range(Balllist2[0]-60,Balllist2[0]) and self.rect[1] in range(Balllist2[1]-60,Balllist2[1]):
            self.kill()
            collisionList[1] = True
        if self.rect[0] in range(Balllist3[0]-60,Balllist3[0]) and self.rect[1] in range(Balllist3[1]-60,Balllist3[1]):
            self.kill()            
            collisionList[2] = True
        if self.rect[0] in range(Balllist4[0]-60,Balllist4[0]) and self.rect[1] in range(Balllist4[1]-60,Balllist4[1]):
            self.kill()            
            collisionList[3] = True
        if self.rect[0] in range(Balllist5[0]-60,Balllist5[0]) and self.rect[1] in range(Balllist5[1]-60,Balllist5[1]):
            self.kill()
            collisionList[4] = True          
        if self.rect[0] in range(Balllist6[0]-60,Balllist6[0]) and self.rect[1] in range(Balllist6[1]-60,Balllist6[1]):
            self.kill()
            collisionList[5] = True
        if self.rect[0] in range(Balllist7[0]-60,Balllist7[0]) and self.rect[1] in range(Balllist7[1]-60,Balllist7[1]):
            self.kill()            
            collisionList[6] = True
        if self.rect[0] in range(Balllist8[0]-60,Balllist8[0]) and self.rect[1] in range(Balllist8[1]-60,Balllist8[1]):
            self.kill()            
            collisionList[7] = True            
        if self.rect[0] in range(Balllist9[0]-60,Balllist9[0]) and self.rect[1] in range(Balllist9[1]-60,Balllist9[1]):
            self.kill()
            collisionList[8] = True          
        if self.rect[0] in range(Balllist10[0]-60,Balllist10[0]) and self.rect[1] in range(Balllist10[1]-60,Balllist10[1]):
            self.kill()
            collisionList[9] = True
        if self.rect[0] in range(Balllist11[0]-60,Balllist11[0]) and self.rect[1] in range(Balllist11[1]-60,Balllist11[1]):
            self.kill()            
            collisionList[10] = True
        if self.rect[0] in range(Balllist12[0]-60,Balllist12[0]) and self.rect[1] in range(Balllist12[1]-60,Balllist12[1]):
            self.kill()            
            collisionList[11] = True
        if self.rect[0] in range(Balllist13[0]-60,Balllist13[0]) and self.rect[1] in range(Balllist13[1]-60,Balllist13[1]):
            self.kill()
            collisionList[12] = True          
        if self.rect[0] in range(Balllist14[0]-60,Balllist14[0]) and self.rect[1] in range(Balllist14[1]-60,Balllist14[1]):
            self.kill()
            collisionList[13] = True
        if self.rect[0] in range(Balllist15[0]-60,Balllist15[0]) and self.rect[1] in range(Balllist15[1]-60,Balllist15[1]):
            self.kill()            
            collisionList[14] = True
        if self.rect[0] in range(Balllist16[0]-60,Balllist16[0]) and self.rect[1] in range(Balllist16[1]-60,Balllist16[1]):
            self.kill()            
            collisionList[15] = True




        if not self.rect.colliderect(screen_rect):
            self.kill()
class Control(object):
    def __init__(self):
        self.screen = pg.display.get_surface()
        self.screen_rect = self.screen.get_rect()
        self.done = False
        self.clock = pg.time.Clock()                                                                                                                          
        self.fps = 60.00
        self.keys = pg.key.get_pressed()
        self.cannon = Turret((250,250))
        self.objects = pg.sprite.Group()
        self.original_ball = TURRET1
        self.ball = self.original_ball.copy()

            
        
        
        
    def event_loop(self,points,name,file,Timer):
        for event in pg.event.get():
            self.keys = pg.key.get_pressed() 
            if event.type == pg.QUIT or self.keys[pg.K_ESCAPE]:
                GameOver(name,points,file,Timer)
            self.cannon.get_event(event, self.objects)

    def update(self,collisionList,points,point,health,Name,HSList,Balllist1,Balllist2,Balllist3,Balllist4,Balllist5,Balllist6,Balllist7,Balllist8,Balllist9,Balllist10,Balllist11,Balllist12,Balllist13,Balllist14,Balllist15,Balllist16):
        self.cannon.update(self.keys)
        self.objects.update(self.screen_rect,collisionList,points,point,health,Name,HSList,Balllist1,Balllist2,Balllist3,Balllist4,Balllist5,Balllist6,Balllist7,Balllist8,Balllist9,Balllist10,Balllist11,Balllist12,Balllist13,Balllist14,Balllist15,Balllist16)
        
        
    def draw(self):
        self.cannon.draw(self.screen)
        self.objects.draw(self.screen)
    def display_fps(self,points,health):
        point = str(points)
        caption = "{} - Points: {:} Health: {:}".format(CAPTION, points,health)
        pg.display.set_caption(caption)
    def main_loop(self,StartGui,difficulty,myfont,collisionList,points,point,health,Name,HSList,Balllist1,Balllist2,Balllist3,Balllist4,Balllist5,Balllist6,Balllist7,Balllist8,Balllist9,Balllist10,Balllist11,Balllist12,Balllist13,Balllist14,Balllist15,Balllist16):
        StartGui.withdraw()
        while not self.done:

            surface = pg.display.get_surface()
            timer = pygame.time.get_ticks()
            Timer = timer/1000
            objects = pygame.sprite.Group()
            self.update(collisionList,points,point,health,Name,HSList,Balllist1,Balllist2,Balllist3,Balllist4,Balllist5,Balllist6,Balllist7,Balllist8,Balllist9,Balllist10,Balllist11,Balllist12,Balllist13,Balllist14,Balllist15,Balllist16)
            self.draw()                        
            ###Movement for balls toward the centre of the screen
            if Timer > 3:
                points, health = ball1(Balllist1,collisionList,points,health,TURRET1)
                points, health = ball2(Balllist2,collisionList,points,health,TURRET1)
                points, health = ball3(Balllist3,collisionList,points,health,TURRET1)
            if Timer > 33:
                points,health = ball4(Balllist4,collisionList,points,health,TURRET1)
                points,health = ball5(Balllist5,collisionList,points,health,TURRET1)
            if Timer > 66:
                points,health = ball6(Balllist6,collisionList,points,health,TURRET1)
                points,health = ball7(Balllist7,collisionList,points,health,TURRET1)
            if Timer > 99:
                points,health = ball8(Balllist8,collisionList,points,health,TURRET1)
                points,health = ball9(Balllist9,collisionList,points,health,TURRET1)
                points,health = ball10(Balllist10,collisionList,points,health,TURRET1)
            if Timer > 200:
                points,health = ball11(Balllist11,collisionList,points,health,TURRET1)
                points,health = ball12(Balllist12,collisionList,points,health,TURRET1)
                points,health = ball13(Balllist13,collisionList,points,health,TURRET1)
            if Timer > 400:
                points,health = ball14(Balllist14,collisionList,points,health,TURRET1)
                points,health = ball15(Balllist15,collisionList,points,health,TURRET1)
                points,health = ball16(Balllist16,collisionList,points,health,TURRET1)
            self.event_loop(points,Name,file,Timer)
            self.clock.tick(self.fps)
            self.display_fps(points,health)
            Timertext = myfont.render("Time: "+str(Timer),1,(255,255,255))
            Healthtext = myfont.render("Health: "+str(health),1,(255,255,255))
            Pointstext = myfont.render("Points: "+str(points),1,(255,255,255))
            surface.blit(Timertext,(900,0))
            surface.blit(Healthtext, (20,0))
            surface.blit(Pointstext, (350,0))
            pg.display.flip()
            if health == 0:
                GameOver(Name,points,file,Timer)

def Start(Name,Difficulty,Tutorial):
    myfont = pygame.font.SysFont('Gill Sans Condensed Ultra Bold',64)

    StartGUI = Tk()
    StartGUI.geometry('300x400')
    StartGUI.title('ArchonDynasty: Shooting Game.')
    ttk.Label(StartGUI,text = 'Name and Difficulty Chooser', font = ('Name and Difficulty Chooser', 17)).grid(column=0,row=0,columnspan=2)
    ttk.Label(StartGUI,text = 'Difficulty:',font = (30)).grid(column=1,row=1)
    ttk.Label(StartGUI,text = 'Name:',font = (30)).grid(column=0,row=1)
    ttk.Button(StartGUI,text = 'Easy',command=Difficulty==2).grid(column=1,row=2)
    ttk.Button(StartGUI,text = 'Medium',command=Difficulty==5).grid(column=1,row=3)
    ttk.Button(StartGUI,text = 'Hard',command=Difficulty==10).grid(column=1,row=4)
    ttk.Button(StartGUI,text = 'Impossible',command=Difficulty==0).grid(column=1,row=5)
    ttk.Label(StartGUI,text = 'Tutorial:',font = (30)).grid(column=0,row=3)
    ttk.Button(StartGUI,text = 'Yes',command=Yes(Tutorial)).grid(column=0,row=4)
    ttk.Button(StartGUI,text = 'No',command=No(Tutorial)).grid(column=0,row=5)
    Name = StringVar()
    ttk.Entry(StartGUI,textvariable=Name).grid(column=0,row=2)
    Name.get()
    ttk.Button(StartGUI,text = 'Start',command=lambda:Control().main_loop(StartGUI,Difficulty,myfont,collisionList,points,point,health,Name,HSList,Balllist1,Balllist2,Balllist3,Balllist4,Balllist5,Balllist6,Balllist7,Balllist8,Balllist9,Balllist10,Balllist11,Balllist12,Balllist13,Balllist14,Balllist15,Balllist16)).grid(column=1,row=6)
    StartGUI.mainloop()
def Yes(Tutorial):
    Tutorial = True
def No(Tutorial):
    Tutorial = False

                        

Start(Name,Difficulty,Tutorial)

                        

