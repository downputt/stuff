import pgzrun
import pygame

WIDTH = 300
HEIGHT = 300

def draw():
    screen.fill((135, 206, 250))

    point1 = (50,150)
    point2 = (150,50)
    point3 = (75,150)
    pygame.draw.polygon([point1, point2, point3], (121, 114, 113))
    point21 = (250,150)
    point22 = (150,50)
    point23 = (225,150)
    pygame.draw.polygon([point21, point22, point23], (121, 114, 113))

    screen.draw.filled_circle((150,75),25,(255,200,100))

    screen.draw.filled_rect(Rect((0,150), (300, 300)), (50, 150, 50))

pgzrun.go()