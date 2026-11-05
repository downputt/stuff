import pygame

pygame.init()

WIDTH = 500
HEIGHT = 500
GRAY = (179,179,179)
GERY = (145,145,145)
RED = (255,107,107)
DARKRED = (207,81,81)
BLUE = (158, 195, 255)

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("spaceship")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    screen.fill((29,28,26))
    pygame.draw.rect(screen, GERY, ((200,200),(100,150)),5)
    pygame.draw.rect(screen, GRAY, ((205,205),(90,140)))
    pygame.draw.circle(screen, GERY, (250,275), 30)
    pygame.draw.circle(screen, BLUE, (250,275), 25)
    pygame.draw.polygon(screen, DARKRED, ((200,200),(300,200),(250,105)))
    pygame.draw.polygon(screen, RED, ((210,195),(290,195),(250,115)))
    pygame.draw.polygon(screen, GERY, ((225,350),(275,350),(270,375),(230,375)))
    pygame.draw.polygon(screen, GRAY, ((230,350),(270,350),(265,370),(235,370)))
    pygame.draw.polygon(screen, RED, ((265,375),(235,375),(250,400)))
    pygame.draw.rect(screen, DARKRED, ((240,310),(15,35)))
    pygame.draw.rect(screen, RED, ((245,315),(5,25)))
    pygame.draw.rect(screen, DARKRED, ((185,310),(15,35)))
    pygame.draw.rect(screen, RED, ((190,315),(5,25)))
    pygame.draw.rect(screen, DARKRED, ((300,310),(15,35)))
    pygame.draw.rect(screen, RED, ((305,315),(5,25)))

    pygame.display.flip()