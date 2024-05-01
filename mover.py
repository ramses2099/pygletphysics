import pyglet

class Mover():
    def __init__(self, batch, image=None, size=0.1, x=0, y=0, vx=0, vy=0):
      self.image = image
      self.sprite
      if self.image:
        self.sprite = pyglet.sprite.Sprite(self.image, batch)
        self.sprite.scale_x = self.sprite.scale_y = 0