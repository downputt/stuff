import pygame

pygame.init()

screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("House")

# Colors

SKY = (155,246,255)
GREEN = (202,255,191)
BROWN = (131,105,83)
RED = (255,173,173)
WHITE = (255,255,252)
YELLOW = (253,255,182)
GREY = (150,150,150)
DRYWALL = (245,210,160)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Sky
    screen.fill(SKY)

    # Sun
    pygame.draw.circle(screen, YELLOW, (700, 90), 45)

    # Clouds
    pygame.draw.circle(screen, WHITE, (120, 90),25)
    pygame.draw.circle(screen, WHITE, (150,75),30)
    pygame.draw.circle(screen, WHITE, (180,90),25)

    pygame.draw.circle(screen, WHITE, (480,100),25)
    pygame.draw.circle(screen, WHITE, (510,85),30)
    pygame.draw.circle(screen, WHITE, (540,100),25)

    # Grass

    pygame.draw.rect(screen,GREEN,(0,400,800,200))

    # Path

    pygame.draw.polygon(screen,GREY,[(340,400),(460,400),(550,600),(250,600)])

    # Drywall

    pygame.draw.rect(screen,DRYWALL,(250,250,300,200))

    # Roof

    pygame.draw.polygon(screen,RED,[(220,260),(400,120),(580,260)])

    # Door

    pygame.draw.rect(screen,BROWN,(370,340,65,110))
    pygame.draw.circle(screen,YELLOW,(420,395),5)

    # LWindow

    pygame.draw.rect(screen,SKY,(280,290,65,60))
    pygame.draw.line(screen,WHITE,(312,290),(312,350),3)
    pygame.draw.line(screen,WHITE,(280,320),(345,320),3)

    # RWindow

    pygame.draw.rect(screen,SKY,(455,290,65,60))
    pygame.draw.line(screen,WHITE,(487,290),(487,350),3)
    pygame.draw.line(screen,WHITE,(455,320),(520,320),3)

    # Tree Trunk

    pygame.draw.rect(screen,BROWN,(100,300,35,120))