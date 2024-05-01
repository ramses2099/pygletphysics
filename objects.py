import pyglet
import pymunk, pymunk.pyglet_util

class Box(object):
    def __init__(self, space, pos, size=(32.0, 32.0)) -> None:
      self.mass = 10
      self.moment = pymunk.moment_for_box(self.mass, size)
      self.body = pymunk.Body(self.mass, self.moment, body_type=pymunk.body.Body.DYNAMIC)
      self.body.position = pymunk.vec2d.Vec2d(pos[0], pos[1])
      self.shape = pymunk.Poly.create_box(self.body, (32, 32))
      space.add(self.body, self.shape)