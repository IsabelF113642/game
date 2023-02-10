man = Actor("characterman")
man.topright = 0, 10

WIDTH = 500
HEIGHT = man.height + 100
speed= 2
import random

def draw():
    screen.fill((128, 0, 0))
    man.draw()


def update():
    global speed
    man.left = man.left + speed
    if man.left > WIDTH:
        speed = speed + .5


def on_mouse_down(pos):
    if man.collidepoint(pos):
        print("Ahhh!")
        sounds.bookdroptrim.play()
        set_man_hurt()
    else:
        print("Haha you missed!")

def set_man_hurt():
    man.image="blob_hurt"
    clock.schedule_unique(set_man_normal, 1)

def set_man_normal():
    man.image="characterman"
