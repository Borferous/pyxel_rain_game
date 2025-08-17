import pyxel
import math
import random
from go.float_text import FloatText

class Tree:
    treeSprite = (16,0)
    fireSprites = [(24,0),(24,8)]
    size = (8,8)
    def __init__(self, position: list):
        self.position = position.copy()
        self.fireTick = 0
        self.isFire = 0
        self.tick = 0
        self.health = 100
        pass

    def update(self, world):
        
        self.tick += 1
        
        onFire = self.isFire > 0
        
        if onFire:
            self.fireTick += 0.1
            if self.tick % 60 == 0:
                self.health -= self.isFire
                if self.health <= 0:
                    world.floatTexts.append(FloatText('-1',self.position, 8))
                    world.lives -= 1
                    world.trees.remove(self)
            
        if not onFire and self.tick % 60 == 0 and random.random() <= 0.1:
            self.isFire = int(random.randint(1,world.difficulty))
                
        
        for r in world.raindrops:
            rx, ry = r.position
            x, y = self.position
            rw, rh = r.size
            w, h = self.size
            if abs(x - rx) < (w + rw) / 2 and abs(y - ry) < (h + rh) / 2:
                
                if onFire:
                    self.isFire -= 1
                    world.raindrops.remove(r)
                    if self.isFire <= 0:
                        reward = 10
                        world.floatTexts.append(FloatText(f'+{reward}',self.position, 10))
                        world.score += reward
                        
                elif self.health < 100:
                    world.floatTexts.append(FloatText('+',self.position, 11))
                    self.health = min(self.health + 5, 100)
                    world.raindrops.remove(r)
                    
            
    def draw(self):
        x, y = self.position
        w, h = self.size
        if self.isFire > 0:        
            sx, sy = self.fireSprites[math.floor(self.fireTick % 2)]
            pyxel.blt(x-w/2,y-h/2,0,sx, sy, w, h, 0)
        else:
            sx, sy = self.treeSprite
            pyxel.blt(x-w/2,y-h/2,0,sx, sy, w, h, 0)
        
        