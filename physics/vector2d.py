from math import sqrt


class Vector2d:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def add(self, v) -> None:
        self.x = self.x + v.x
        self.y = self.y + v.y

    def sub(self, v) -> None:
        self.x = self.x - v.x
        self.y = self.y - v.y

    def mult(self, n) -> None:
        self.x = self.x * n
        self.y = self.y * n

    def div(self, n) -> None:
        self.x = self.x / n
        self.y = self.y / n

    def mag(self) -> float:
        return sqrt((self.x * self.x) + (self.y * self.y))
    
    def normalize(self):
        m = self.mag
        if(m > 0):
            self.div(m)
    
    def limit(self, max):
        if(self.mag() > max):
            self.normalize()
            self.mult(max)
  