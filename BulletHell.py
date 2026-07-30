import pgzrun
import random
import sys

WIDTH = 500
HEIGHT = 500

star = Actor("star")
star.pos = (100,50)

star1 = Actor("star")
star1.pos = (250,50)

star2 = Actor("star")
star2.pos = (400,50)

star3 = Actor("star")
star3.pos = (300,50)

star4 = Actor("star")
star4.pos = (200,50)

star5 = Actor("star")
star5.pos = (500,50)

star6 = Actor("star")
star6.pos = (350,50)

star7 = Actor("star")
star7.pos = (500,50)

star8 = Actor("star")
star8.pos = (0,50)

star9 = Actor("star")
star9.pos = (150,50)

ship = Actor("spaceship")
ship.pos = (250,400)

def draw():
    screen.clear()
    screen.fill((29,28,26))
    ship.draw()
    star.draw()
    star1.draw()
    star2.draw()
    star3.draw()
    star4.draw()
    star5.draw()
    star6.draw()
    star7.draw()
    star8.draw()
    star9.draw()

def update():
    if keyboard.left:
        ship.x -= 5
    elif keyboard.right:
        ship.x += 5
    
    if ship.x > 500:
        ship.x = 0
    
    elif ship.x < 0:
        ship.x = 500
    
    star.y += 4
    star1.y += 4.5
    star2.y += 5
    star3.y += 5.5
    star4.y += 6
    star5.y += 6.5
    star6.y += 7
    star7.y += 7.5
    star8.y += 8
    star9.y += 9

    if star.y > 500:
        x = random.randint(0,500)
        star.y = 0
        star.x = x
    
    elif star1.y > 500:
        x = random.randint(0,500)
        star1.y = 0
        star1.x = x
    
    elif star2.y > 500:
        x = random.randint(0,500)
        star2.y = 0
        star2.x = x

    elif star3.y > 500:
        x = random.randint(0,500)
        star3.y = 0
        star3.x = x
    
    elif star4.y > 500:
        x = random.randint(0,500)
        star4.y = 0
        star4.x = x

    elif star5.y > 500:
        x = random.randint(0,500)
        star5.y = 0
        star5.x = x

    elif star6.y > 500:
        x = random.randint(0,500)
        star6.y = 0
        star6.x = x
    
    elif star7.y > 500:
        x = random.randint(0,500)
        star7.y = 0
        star7.x = x
    
    elif star8.y > 500:
        x = random.randint(0,500)
        star8.y = 0
        star8.x = x
    
    elif star9.y > 500:
        x = random.randint(0,500)
        star9.y = 0
        star9.x = x

    if ship.x == star.x and ship.y == star.y:
        sys.exit()
    
    elif ship.x == star1.x and ship.y == star1.y:
        sys.exit()
    
    elif ship.x == star2.x and ship.y == star2.y:
        sys.exit()
    
    elif ship.x == star3.x and ship.y == star3.y:
        sys.exit()
    
    elif ship.x == star4.x and ship.y == star4.y:
        sys.exit()
    
    elif ship.x == star5.x and ship.y == star5.y:
        sys.exit()

    elif ship.x == star6.x and ship.y == star6.y:
        sys.exit()
    
    elif ship.x == star7.x and ship.y == star7.y:
        sys.exit()
    
    elif ship.x == star8.x and ship.y == star8.y:
        sys.exit()
    
    elif ship.x == star9.x and ship.y == star9.y:
        sys.exit()

pgzrun.go()