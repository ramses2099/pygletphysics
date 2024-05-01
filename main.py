import pyglet
import random

# PEP 8 - Style Guide for Python
from constants import *
from physics import *
from physics.helpers import *

window = pyglet.window.Window(
    width=WIDTH, height=HEIGHT, caption=TITLE, resizable=False
)
batch = pyglet.graphics.Batch()

p = Particula(WIDTH/2, HEIGHT/2, batch)

mainparticle = []
countparticle = 5

for i in range(countparticle):
    position = random2d(16, 700)
    color = random_color()
    radius = random.randint(16, 32)
    pa = Particula(position.x, position.y, batch, radius, color)
    mainparticle.append(pa)

@window.event
def on_draw():
    window.clear()
    batch.draw()


def update(dt):
    pass


if __name__ == "__main__":
    # game loop
    pyglet.clock.schedule_interval(update, FPS)
    pyglet.app.run()
