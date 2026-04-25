import pygame as pg
import time
import Constants as Const
import ScreenManager

last_time = time.time()
screen = ScreenManager.ScreenManager()
run = True
while run:
    time.sleep(max(0.0, last_time - time.time() + 1/Const.FPS))
    last_time = time.time()
    screen.update()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False