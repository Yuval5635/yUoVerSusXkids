'''
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
        print("main28: level up to: ", game.level)

    pgUtils.PygameUtils.update()
    game.update()
    win.update_window(game)
'''
import os
import subprocess
from py4j.java_gateway import JavaGateway, GatewayParameters, launch_gateway

BASE = os.path.dirname(os.path.abspath(__file__))

JAVA_SRC = os.path.join(BASE, "java", "src")
JAVA_OUT = os.path.join(BASE, "java", "out")
PY4J_JAR = os.path.join(BASE, "lib", "py4j.jar")

subprocess.run([
    "javac",
    "-d", JAVA_OUT,
    "-cp", PY4J_JAR,
    JAVA_SRC + "/*.java"
], shell=True)

port = launch_gateway(classpath=JAVA_OUT)

gateway = JavaGateway(gateway_parameters=GatewayParameters(port=port))

main = gateway.jvm.Main()
