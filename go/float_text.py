
import pyxel

class FloatText:
    def __init__(self, text: str, position: list, color: int):
        self.text = text
        self.position = position.copy()
        self.life = 60
        self.color = color
        pass
    
    def update(self, world):
        
        self.life -= 1
        if self.life <= 0:
            world.floatTexts.remove(self)
        
        self.position[1] -= int(self.life * 0.05)
        pass
        
    def draw(self):
        x, y = self.position
        if self.life > 30 or self.life % 10 < 5:
            pyxel.text(x, y, self.text, self.color)
        pass
        
    