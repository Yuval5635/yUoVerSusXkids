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
        for button in Button.get_buttons():
            if button.is_pressed:
                color = button.press_color
            elif button.is_hover:
                color = button.hover_color
            else:
                color = button.color
            pg.draw.rect(window, color, pg.Rect(button.pos.x, button.pos.y, button.width, button.height), border_radius=button.radius)

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