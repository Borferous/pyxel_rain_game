import pyxel
import random
from util import lerp

from go.float_text import FloatText
from go.player import Player
from go.rain_drop import RainDrop
from go.tree import Tree

from go.menu import Menu
from go.display_text import DisplayText

TITLE = "Would you lose? Nah i'd rain"

class Scene:
    game = 'game'
    menu = 'menu'
    lose = 'lose'
    about = 'about'
    howtoplay = 'howtoplay'
    
class App:
    
    def startGame(self):
        self.setScene(Scene.game)
        self.gametick = 0
        self.player = Player()
        self.raindrops = []
        self.floatTexts = []
        self.difficulty = 1
        self.isPause = False
        self.trees = [
            Tree([int(random.randint(0,256)), 128]),
            Tree([int(random.randint(0,256)), 128]),
            Tree([int(random.randint(0,256)), 128]),
        ]
        self.score = 0
        self.lives = 5
        pass
    
    def gotoAbout(self):
        self.setScene(Scene.about)
        self.uiElements = [
            DisplayText([124,124])
                .newLine(TITLE, 1)
                .newLine("By: Bruhder Boi")
                .newLine("a submission for the mini jam 191:sky!")
                .newLine("with the limitation: constant descent!")
                .newLine("In this game trees burn for absolutely no reason")
                .newLine("Extinguish the fire to protect the trees")
                .newLine("This is my first game with pyxel")
        ,Menu([124,124 + 64]).Option("Go Back", self.gotoMenu)]
        
    def howToPlay(self):
        self.setScene(Scene.howtoplay)
        self.uiElements = [
            DisplayText([124,124])
                .newLine("How to play!", 10)
                .newLine("Press the A/D key or the arrow keys to move")
                .newLine("Press the P to pause and unpause the game")
                .newLine("Press SPACE to spray rain  but it consumes score")
                .newLine("Trees burst into flames for some reason")
                .newLine("extinguish the flames to save the trees")
                .newLine("you can heal trees with your rain")
                .newLine("lose 5 trees, and you lose!", 8)
        ,Menu([124,124 + 64]).Option("Go Back", self.gotoMenu)]
    
    def gotoMenu(self):
        self.setScene(Scene.menu)
        self.uiElements = [(
            Menu([124,124])
                .Title(TITLE)
                .Option('Start Game', self.startGame)
                .Option('How to play', self.howToPlay)
                .Option('About', self.gotoAbout)
        )]
    
    def youLose(self):
        self.setScene(Scene.lose)
        self.uiElements = [(
            Menu([124,124])
                .Title(f"Score: {self.score}")
                .Option("Play Again", self.startGame)
                .Option('Back to Menu', self.gotoMenu)
        )]
            
    def setScene(self, newScene):
        self.transition = 1
        self.uiElements = []
        self.scene = newScene
    
    def __init__(self):
        self.transition = 0
        self.windowSize = (256, 256)
        self.uiElements = []
        self.gotoMenu()
        pyxel.init(self.windowSize[0], self.windowSize[1], title=TITLE, fps=60, quit_key= pyxel.KEY_ESCAPE)
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
            if not self.isPause:
                self.gametick += 1
                if self.everySec(0.15):
                    if pyxel.btn(pyxel.KEY_SPACE) and self.score > 0:
                        self.score -= 1
                        for i in range(3):
                            self.raindrops.append(RainDrop(self.player.position, i - 1))
                    else:
                        self.raindrops.append(RainDrop(self.player.position, 0))
                        
                if self.everySec(10) and self.difficulty < 10:
                    self.difficulty += 1
                    
                if self.everySec(5) and len(self.trees) < 20:
                    self.trees.append(Tree([int(random.randint(0,256)), 128]))
                    
                self.updateEntts(self.raindrops)
                self.updateEntts(self.trees)
                self.updateEntts(self.floatTexts)
                self.player.update()
            
            if pyxel.btnp(pyxel.KEY_P):
                self.isPause = not self.isPause
        
        for ui in self.uiElements:
            ui.update()
        
        if self.transition > 0:
            self.transition -= 0.02

    def draw(self):
        pyxel.cls(5)
        
        # Ground
        pyxel.rect(0, 128 + 4, 256, 128, 3)
        for i, d in enumerate([0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 1]):
            pyxel.dither(d)
            pyxel.rect(0, 128 + 4 + 16 * (i + 1), 256, 16, 1)
        pyxel.dither(1)
        
        if self.scene == Scene.game:
            self.drawEntts(self.raindrops)
            self.drawEntts(self.trees)
            self.drawEntts(self.floatTexts)
            self.player.draw()
             
            pyxel.rect(0, 0, 256, 10, 0)
            scoreText = f"SCORE: {self.score:05}"
            pyxel.text(2, 2, scoreText, 7)
            
            # Top Bar
            if self.lives <= 0:
                self.youLose()
            for i in range(self.lives):
                pyxel.blt(256 - ((i + 1) * 10), 1, 0, 16, 0, 8, 8, 0)
                
            
            if self.isPause:
                text = "PAUSED"
                x = pyxel.width // 2 - (len(text) * 4) // 2
                y = 24
                pyxel.text(x, y, text, 0)

        for ui in self.uiElements:
            ui.draw()

        pyxel.dither(self.transition)
        pyxel.rect(0,0,256,256,0)
        pyxel.dither(1)
    
    def everySec(self,sec):
        return self.gametick % int(60 * sec) == 0
    
App()