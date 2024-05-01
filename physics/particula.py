import pyglet
from .shape import Circle
from .vector2d import Vector2d


class Particula:
    def __init__(self, x, y, batch, r=16, color=(255, 255, 255)):
        self.batch = batch
        self.body = Circle(x, y, r)
        self.color = color
        self.position = Vector2d(x, y)
        self.velocity = Vector2d()
        # pyglet object
        self.shape = pyglet.shapes.Circle(
            self.position.x, self.position.y, self.body.r, color=self.color, batch=self.batch
        )

    def update(self, dt) -> None:
        pass
