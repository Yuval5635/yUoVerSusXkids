import math
import pygame as pg
import Constants.Graphics as GraphicConst
import Constants as Const

class Graphics:
    def __init__(self):
        self.win = pg.display.set_mode((Const.WINDOW_WIDTH, Const.WINDOW_HEIGHT))
        pg.display.set_caption("You VS x kids")
        self.font = pg.font.Font("Fonts/PixelifySans-Regular.ttf", 40)

    def draw_sector(self, color, center, radius, start_angle, end_angle):
        temp = pg.Surface((radius * 2, radius * 2), pg.SRCALPHA)

        # draw full circle
        pg.draw.circle(temp, color, (radius, radius), radius)

        # build mask polygon
        points = [(radius, radius)]

        for angle in range(start_angle, end_angle + 1):
            rad = math.radians(angle)
            x = radius + radius * math.cos(rad)
            y = radius + radius * math.sin(rad)
            points.append((x, y))

        # remove outside
        mask = pg.Surface((radius * 2, radius * 2), pg.SRCALPHA)
        pg.draw.polygon(mask, (255, 255, 255), points)

        temp.blit(mask, (0, 0), special_flags=pg.BLEND_RGBA_MULT)

        self.win.blit(temp, (center[0] - radius, center[1] - radius))

    def update_window(self, game): #EntityContainer
        self.win.fill(GraphicConst.BACKGROUND_COLOR)

        # need to change for images
        pg.draw.rect(self.win, (0, 0, 255), pg.Rect(game.player.pos.x - (GraphicConst.PLAYER_WIDTH // 2), game.player.pos.y - (GraphicConst.PLAYER_HEIGHT // 2), GraphicConst.PLAYER_WIDTH, GraphicConst.PLAYER_HEIGHT))
        for enemy in game.enemies:
            pg.draw.rect(self.win, (255, 0, 0), pg.Rect(enemy.pos.x - (GraphicConst.ENEMY_WIDTH // 2), enemy.pos.y - (GraphicConst.ENEMY_HEIGHT // 2), GraphicConst.ENEMY_WIDTH, GraphicConst.ENEMY_HEIGHT))

        pg.display.update()