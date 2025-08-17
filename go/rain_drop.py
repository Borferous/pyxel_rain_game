import pyxel
import random

class RainDrop:
    sprites = [(0,8),(8,8)]
    size = [8,8]
    def __init__(self, position: list, xvel: int):
        self.velocity = [xvel, 2]
        self.sprite = random.choice(self.sprites)
        sx, sy = position[0] + random.randint(-3,3), position[1]
        self.position = [sx, sy]
        self.life = 60
        
    
    def update(self, world):
        
        if self.position[1] > 124 + 8:
            world.raindrops.remove(self)
            
        self.position[0] += self.velocity[0]
        self.position[1] += self.velocity[1]
        
    def draw(self):
        u, v = self.sprite
        x, y = self.position
        w, h = self.size
        pyxel.blt(x - w / 2 , y - h / 2,0 , u,v ,w, h,0)
    