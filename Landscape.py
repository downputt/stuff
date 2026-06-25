import pgzrun

WIDTH = 300
HEIGHT = 300

def draw():
    screen.fill((135, 206, 250))

    screen.draw.filled_circle((150,75),25,(255,200,100))

    screen.draw.filled_rect(Rect((0,150), (300, 300)), (50, 150, 50))

    screen.draw.filled_rect(Rect((125,150), (50,300)), (77, 148, 255))

pgzrun.go()