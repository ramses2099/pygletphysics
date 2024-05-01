from math import sqrt
from random import randint
from .shape import *
from .vector2d import Vector2d

def collideBox(rect1:Rectangle, rect2:Rectangle) -> bool:
    if( rect1.x < rect2.x + rect2.w 
        and rect1.x + rect1.w > rect2.x 
        and rect1.y < rect2.y + rect2.h
        and rect1.y +rect1.h > rect2.y):
        return True
    return False
  
def collideCircle(circ1:Circle, circ2: Circle) -> bool:
    dx = circ1.x - circ2.x
    dy = circ1.y - circ2.y
    dist = sqrt((dx*dx) + (dy*dy))
    if(dist < circ1.r + circ2.r):
        return True
    return False

def random2d(min, max) -> Vector2d:
    x = randint(min, max)
    y = randint(min, max)
    return Vector2d(x, y)

def random_color() -> tuple:
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return (r, g, b)