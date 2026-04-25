import Constants
import EntityContainer
import pygame as pg
import Utils.PygameUtils as pgUtils
from Graphics import Graphics
from Utils.Buttons.Button import Button
from Utils.Buttons.SquareButton import SquareButton
from Utils.UtilsManager import Utils
from Utils.Vector import Vector


class ScreenManager:
    def __init__(self):
        self.win = Graphics.Graphics()
        self.game = EntityContainer.EntityContainer()
        self.current_screen = Constants.ScreenState.START
        self.last_screen = None
        SquareButton("Starting Button", Vector(Constants.WINDOW_WIDTH / 2, Constants.WINDOW_HEIGHT * 0.75), 200, 30,(0, 0, 0), radius=5)

    def update(self):

        #update
        Utils.update()
        if self.current_screen == Constants.ScreenState.GAME:
            self.game.update()
            self.win.update_game(self.game)
        elif self.current_screen == Constants.ScreenState.START:
            self.win.update_starting_game()
        elif self.current_screen == Constants.ScreenState.GAME_OVER:
            self.win.update_game_over()
        elif self.current_screen == Constants.ScreenState.PAUSE:
            self.win.update_pause()



        #change screen state if needed
        if self.current_screen == Constants.ScreenState.START:
            if Button.get_buttons()["Starting Button"].is_pressed:
                self.current_screen = Constants.ScreenState.GAME

        elif self.current_screen == Constants.ScreenState.GAME:
            if pgUtils.PygameUtils.is_key_pressed(pg.K_ESCAPE):
                self.current_screen = Constants.ScreenState.PAUSE
            elif not self.game.is_player_alive:
                self.current_screen = Constants.ScreenState.GAME_OVER

        elif self.current_screen == Constants.ScreenState.PAUSE:
            if pgUtils.PygameUtils.is_key_pressed(pg.K_ESCAPE):
                self.current_screen = Constants.ScreenState.GAME

        elif self.current_screen == Constants.ScreenState.GAME_OVER:
            if Button.get_buttons()["Try again"].is_pressed:
                self.current_screen = Constants.ScreenState.GAME
            elif Button.get_buttons()["Go to start"].is_pressed:
                self.current_screen = Constants.ScreenState.START



        #one time generating in screen state
        if self.current_screen != self.last_screen:
            print("ScreenManager50:", self.current_screen)
            if self.last_screen == Constants.ScreenState.START:
                Button.remove_button(Button.get_buttons()["Starting Button"])
                if self.current_screen == Constants.ScreenState.GAME:
                    self.game.start_level()

            elif self.last_screen == Constants.ScreenState.GAME:
                if self.current_screen == Constants.ScreenState.GAME_OVER:
                    SquareButton("Go to start", Vector(Constants.WINDOW_WIDTH * 0.25, Constants.WINDOW_HEIGHT * 0.75), 200, 30, (0, 0, 0), radius=5)
                    SquareButton("Try again", Vector(Constants.WINDOW_WIDTH * 0.75, Constants.WINDOW_HEIGHT * 0.75), 200, 30, (0, 0, 0), radius=5)

            elif self.last_screen == Constants.ScreenState.GAME_OVER:
                Button.remove_button(Button.get_buttons()["Go to start"])
                Button.remove_button(Button.get_buttons()["Try again"])
                if self.current_screen == Constants.ScreenState.START:
                    SquareButton("Starting Button", Vector(Constants.WINDOW_WIDTH / 2, Constants.WINDOW_HEIGHT * 0.75), 200, 30, (0, 0, 0), radius=5)


            self.last_screen = self.current_screen
