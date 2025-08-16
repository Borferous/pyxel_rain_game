import pyxel
import random

from go.float_text import FloatText
from go.player import Player
from go.rain_drop import RainDrop
from go.tree import Tree

class App:
    def __init__(self):
        self.windowSize = (256, 256)
        self.gametick = 0
        
        self.player = Player()
        self.raindrops = []
        self.floatTexts = []
        self.trees = []
        self.score = 0
        
        pyxel.init(self.windowSize[0], self.windowSize[1], title="My App", fps=60, quit_key= pyxel.KEY_ESCAPE)
        pyxel.load("my_res.pyxres")
        pyxel.run(self.update, self.draw)
        
        
        
    def update(self):
        self.gametick += 1
        
        if self.everySec(0.15):
            pos = self.player.position
            self.raindrops.append(RainDrop(pos))
            
        if self.everySec(1) and len(self.trees) < 10:
            sx, sy = int(random.randint(0,256)), 128
            self.trees.append(Tree([sx, sy]))
            
        for r in self.raindrops:
            r.update(self)
            
        for t in self.trees:
            t.update(self)
            
        for t in self.floatTexts:
            t.update(self)
        
        self.player.update()
        
        pass

    def draw(self):
        pyxel.cls(5)
        
        for r in self.raindrops:
            r.draw()
            
        for t in self.trees:
            t.draw()
            
        for t in self.floatTexts:
            t.draw()
            
        pyxel.rect(0, 0, 256, 8, 0)
        scoreText = f"SCORE: {self.score:05}"
        pyxel.text(1,1,scoreText, 7)
        pyxel.rect(0, 128 + 4, 256, 128, 3)
        self.player.draw()
        
        pass
    
    def everySec(self,sec):
        return self.gametick % int(60 * sec) == 0
    
        

App()