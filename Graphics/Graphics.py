import pygame as pg
from Constants import Graphics as GraphicConst
import Constants as Const
from Utils.UtilsManager import Utils


class Graphics:
    def __init__(self):
        pg.init()
        font = pg.font.Font("Graphics/Fonts/PixelifySans-Regular.ttf", 40)
        self.win = pg.display.set_mode((Const.WINDOW_WIDTH, Const.WINDOW_HEIGHT))
        pg.display.set_caption("You VS x kids")

    def update(self):
        Utils.draw(self.win)
        pg.display.update()

    def update_game(self, game): #EntityContainer
        self.win.fill(GraphicConst.BACKGROUND_COLOR)

        # need to change for images
        pg.draw.rect(self.win, (0, 0, 255), pg.Rect(game.player.pos.x - (GraphicConst.PLAYER_WIDTH // 2), game.player.pos.y - (GraphicConst.PLAYER_HEIGHT // 2), GraphicConst.PLAYER_WIDTH, GraphicConst.PLAYER_HEIGHT))
        for enemy in game.enemies:
            pg.draw.rect(self.win, (255, 0, 0), pg.Rect(enemy.pos.x - (GraphicConst.ENEMY_WIDTH // 2), enemy.pos.y - (GraphicConst.ENEMY_HEIGHT // 2), GraphicConst.ENEMY_WIDTH, GraphicConst.ENEMY_HEIGHT))

        self.update()

    def update_starting_game(self):
        self.win.fill(GraphicConst.BACKGROUND_COLOR)
        self.update()

    def update_game_over(self):
        self.update()

    def update_pause(self):
        self.update()