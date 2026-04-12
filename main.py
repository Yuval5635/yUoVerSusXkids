import Graphics.Graphics as Graphics
win = Graphics.Graphics()

print(win)
import EntityContainer
import pygame as pg
import time
import Constants as Const
import Utils.PygameUtils as pgUtils

game = EntityContainer.EntityContainer()
game.start_level()
last_time = time.time()
run = True
while run:
    run = game.is_player_alive
    time.sleep(max(0.0, last_time - time.time() + 1/Const.FPS))
    last_time = time.time()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                run = False
    if game.is_enemies_dead():
        game.set_level(game.level + 1)
        game.start_level()
        print("main27: level up to: ", game.level)

    pgUtils.PygameUtils.update()
    game.update()
    win.update_window(game)