import pgzrun

WIDTH = 500
HEIGHT = 500

star = Actor("star")

ship = Actor("spaceship")
ship.pos(250,400)

def draw():
    screen.fill((0,0,0))
    ship.draw()

pgzrun.go()