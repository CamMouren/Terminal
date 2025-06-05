import pyxel
from player import player
from debug import debug_mode

class Enemi():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.base_speed = 1
        self.speed = 1
        self.base_life = 1
        self.life = 1
        self.width = 8
        self.height = 16
        self.color = pyxel.COLOR_PURPLE


    
    def move(self):
        if self.y > player.y:
            self.y -= self.speed
        if self.y < player.y:
            self.y += self.speed
        if self.x < player.x:
            self.x += self.speed
        if self.x > player.x:
            self.x -= self.speed


    def update(self):
        self.move()

    def draw(self):
        pyxel.rect(self.x, self.y, self.width, self.height, self.color)

ENemi = Enemi()