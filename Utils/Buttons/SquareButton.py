import pygame as pg

from Utils.Buttons.Button import Button
from Utils.PygameUtils import PygameUtils


class SquareButton(Button):
    def __init__(self, name, pos, width, height, color, hover_color=None, press_color=None, radius=0):
        super().__init__(name, pos, color, hover_color, press_color)
        self.width = width
        self.height = height
        self.radius = radius

    @staticmethod
    def draw(window):
        buttons = Button.get_buttons()
        for button in Button.get_buttons():
            if isinstance(buttons[button], SquareButton):
                if buttons[button].is_pressed:
                    color = buttons[button].press_color
                elif buttons[button].is_hover:
                    color = buttons[button].hover_color
                else:
                    color = buttons[button].color
                pg.draw.rect(window, color, pg.Rect(buttons[button].pos.x, buttons[button].pos.y, buttons[button].width, buttons[button].height), border_radius=buttons[button].radius)

    @staticmethod
    def update():
        mouse = PygameUtils.get_mouse_position()
        buttons = Button.get_buttons()
        for button in buttons:
            if isinstance(buttons[button], SquareButton):
                if (buttons[button].pos.x < mouse.x < buttons[button].pos.x + buttons[button].width) and (buttons[button].pos.y < mouse.y < buttons[button].pos.y + buttons[button].height):
                    buttons[button].is_hover = True
                    if PygameUtils.is_mouse_pressed(0):
                        buttons[button].is_pressed = True
                    else:
                        buttons[button].is_pressed = False
                else:
                    buttons[button].is_hover = False