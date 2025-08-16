import pyxel
import random
from util import lerp

from go.float_text import FloatText
from go.player import Player
from go.rain_drop import RainDrop
from go.tree import Tree

from go.menu import Menu

class Scene:
    game = 'game'
    menu = 'menu'
    lose = 'lose'

class App:
    
    def startGame(self):
        self.setScene(Scene.game)
        self.gametick = 0
        self.player = Player()
        self.raindrops = []
        self.floatTexts = []
        self.trees = []
        self.score = 0
        self.lives = 5
        pass
    
    def gotoMenu(self):
        self.setScene(Scene.menu)
        self.startMenu = (
            Menu([124,124])
                .Title('Rain Game Thingy')
                .Option('Start Game', self.startGame)
        )
        pass
    
    def youLose(self):
        self.setScene(Scene.lose)
        self.loseMenu = (
            Menu([124,124])
                .Title("You Lose")
                .Option("Play Again", self.startGame)
                .Option('Back to Menu', self.gotoMenu)
        )
    
    def setScene(self, newScene):
        self.transition = 1
        self.scene = newScene
    
    def __init__(self):
        self.transition = 0
        self.windowSize = (256, 256)
        self.gotoMenu()
        pyxel.init(self.windowSize[0], self.windowSize[1], title="My App", fps=60, quit_key= pyxel.KEY_ESCAPE)
        pyxel.load("my_res.pyxres")
        pyxel.run(self.update, self.draw)
        
    def updateEntts(self, entts):
        for e in entts:
            e.update(self)
            
    def drawEntts(self, entts):
        for e in entts:
            e.draw()
        
    def update(self):
        
        if self.scene == Scene.game:
            self.gametick += 1
            if self.everySec(0.15):
                self.raindrops.append(RainDrop(self.player.position))
            if self.everySec(1) and len(self.trees) < 25:
                self.trees.append(Tree([int(random.randint(0,256)), 128]))
            self.updateEntts(self.raindrops)
            self.updateEntts(self.trees)
            self.updateEntts(self.floatTexts)
            self.player.update()
        elif self.scene == Scene.menu:
            self.startMenu.update()
        elif self.scene == Scene.lose:
            self.loseMenu.update()
        
        if self.transition > 0:
            self.transition -= 0.02

    def draw(self):
        pyxel.cls(5)
        
        if self.scene == Scene.game:
            self.drawEntts(self.raindrops)
            self.drawEntts(self.trees)
            self.drawEntts(self.floatTexts)
            self.player.draw()
             
            pyxel.rect(0, 0, 256, 8, 0)
            scoreText = f"SCORE: {self.score:05}"
            pyxel.text(1, 1, scoreText, 7)
            
            if self.lives <= 0:
                self.youLose()

            for i in range(self.lives):
                pyxel.blt(256 - ((i + 1) * 10), 0, 0, 16, 0, 8, 8, 0)

            # Ground base
            pyxel.rect(0, 128 + 4, 256, 128, 3)

            for i, d in enumerate([0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 1]):
                pyxel.dither(d)
                pyxel.rect(0, 128 + 4 + 16 * (i + 1), 256, 16, 1)

            pyxel.dither(1)

            
        elif self.scene == Scene.menu:
            self.startMenu.draw()
            
        elif self.scene == Scene.lose:
            self.loseMenu.draw()

        pyxel.dither(self.transition)
        pyxel.rect(0,0,256,256,0)
        pyxel.dither(1)
    
    def everySec(self,sec):
        return self.gametick % int(60 * sec) == 0
    
App()