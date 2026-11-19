import pygame

pygame.init()

WIDTH = 500
HEIGHT = 500

screen = pygame.display.set_mode((WIDTH,HEIGHT))

pygame.display.set_caption("soulmove")

clock = pygame.time.Clock()

x = 250
y = 250

soul = pygame.image.load("images/undsoul.png")
soul = pygame.transform.scale(soul, (37, 28))
speed = 5

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x -= speed
    if keys[pygame.K_RIGHT]:
        x += speed
    if keys[pygame.K_UP]:
        y -= speed
    if keys[pygame.K_DOWN]:
        y += speed
        
    screen.fill((0, 0, 0))
    screen.blit(soul, (x, y))
    pygame.display.flip()
    clock.tick(20)

pygame.quit()