import pygame as pg
import random

class MatrixLetters:
    def __init__(self, app):
        self.app = app
        self.letters = "\u30f3\u30ef\u30e9\u30e4\u30de\u30cf\u30ca\u30bf\u30b5\u30ab\u30a2\u30ea\u30df\u30d2\u30cb\u30c1\u30b7\u30ad\u30a4\u30eb\u30e6\u30e0\u30d5\u30cc\u30c4\u30b9\u30af\u30a6\u30ec\u30e1\u30d8\u30cd\u30c6\u30bb\u30b1\u30a8\u30f2\u30ed\u30e8\u30e2\u30db\u30ce\u30c8\u30bd\u30b3\u30aa"
        self.font_size = 10
        self.font = pg.font.SysFont('mikachanpuchimikachanpuchib', self.font_size, bold=True)
        self.columns = app.WIDTH // self.font_size
        self.drops = [1 for i in range(0, self.columns)]

    def draw(self):
        for i in range(0, len(self.drops)):
            char = random.choice(self.letters)
            char_render = self.font.render(char, False, (0,255,0))
            pos = i * self.font_size, (self.drops[i] - 1) * self.font_size
            self.app.surface.blit(char_render, pos)
            if self.drops[i] * self.font_size > app.HEIGHT and random.uniform(0,1) > 0.975:
                self.drops[i] = 0
            self.drops[i] = self.drops[i] + 1

    def run(self):
        self.draw()


class MatrixApp:
    def __init__(self): 
        self.RES = self.WIDTH, self.HEIGHT = 1000, 700
        pg.init()
        self.screen = pg.display.set_mode(self.RES) 
        self.surface = pg.Surface(self.RES, pg.SRCALPHA) 
        self.clock = pg.time.Clock() 
        self.matrixLetters = MatrixLetters(self) 

    def draw(self): 
        self.surface.fill((0,0,0,10))
        self.matrixLetters.run()
        self.screen.blit(self.surface, (0,0))

    def run(self): 
        while True:
            self.draw() 
            [exit() for i in pg.event.get() if i.type == pg.QUIT]
            pg.display.flip() 
            self.clock.tick(30) 

if __name__ == '__main__':
    app = MatrixApp()
    app.run()
