import pygame
import os
import time

pygame.init()

pygame.mixer.init()

WIDTH = 500
HEIGHT = 500

screen = pygame.display.set_mode((WIDTH,HEIGHT))

pygame.display.set_caption("Block Thing")

still = pygame.image.load("block/still/still.png").convert_alpha()

def loadframes(folder):
    frames = []
    files = os.listdir("block/" + folder)
    files.sort()
    for file in files:
        if file.endswith(".png"):
            image = pygame.image.load("block/" + folder + "/" + file).convert_alpha()
            frames.append(image)

    return frames

move = loadframes("move")
trans = loadframes("transition")
impac = loadframes("impact")
impsoun = pygame.mixer.Sound("sounds/PARRY.mp3")
impsoun2 = pygame.mixer.Sound("SOUNDS/UKexplod.mp3")
x = 100
y = 200
speed = 5
curframe = 0
animdel = 0.0625
state = "still"
nexstate = "still"
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    moving = (
        keys[pygame.K_LEFT] or
        keys[pygame.K_RIGHT] or
        keys[pygame.K_UP] or
        keys[pygame.K_DOWN]
    )

    if state == "still" and moving:
        state = "transition"
        nexstate = "move"
        curframe = 0

    elif state == "move" and not moving:
        state = "impact"
        next