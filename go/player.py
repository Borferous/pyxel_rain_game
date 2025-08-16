import pyxel
from util import clamp

class Player:
    def __init__(self):
        self.sprite = [0,0]
        self.size = [16,8]
        self.position = [128,64]
        self.speed = 2
    
    def update(self):
        self.position[0] += (pyxel.btn(pyxel.KEY_D) - pyxel.btn(pyxel.KEY_A)) * self.speed
        # self.position[0] = clamp(self.position[0], self.size[0] / 2, 256 - self.size[0] / 2)
        
        if self.position[0] < -self.size[0]:
            self.position[0] = 256 + self.size[0]
        elif self.position[0] > 256 + self.size[0]:
            self.position[0] = -self.size[0]
    
    def draw(self):
        x, y = self.position
        w, h = self.size
        pyxel.blt(x-w/2,y-h/2,0, self.sprite[0], self.sprite[1] , self.size[0], self.size[1], 0)
        
    