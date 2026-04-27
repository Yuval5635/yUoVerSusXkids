import pygame as pg
import time
import Constants as Const
import ScreenManager
from Utils import PygameUtils

last_time = time.time()
screen = ScreenManager.ScreenManager()
run = True
while run:
    time.sleep(max(0.0, last_time - time.time() + 1/Const.FPS))
    last_time = time.time()
    screen.update()
    for event in PygameUtils.PygameUtils.events:
        if event.type == pg.QUIT:
            run = False