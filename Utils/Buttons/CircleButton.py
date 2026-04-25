from Utils.Buttons.Button import Button
import pygame as pg

from Utils.PygameUtils import PygameUtils


class CircleButton(Button):
    def __init__(self, name, pos, radius, color, hover_color=None, press_color=None):
        super().__init__(name, pos, color, hover_color, press_color)
        self.radius = radius

    @staticmethod
    def draw(window):
        buttons = Button.get_buttons()
        for button in Button.get_buttons():
            if isinstance(buttons[button], CircleButton):
                if buttons[button].is_pressed:
                    color = buttons[button].press_color
                elif buttons[button].is_hover:
                    color = buttons[button].hover_color
                else:
                    color = buttons[button].color
                pg.draw.circle(window, color, (buttons[button].pos.x, buttons[button].pos.y), buttons[button].radius)

    @staticmethod
    def update():
        mouse = PygameUtils.get_mouse_position()
        buttons = Button.get_buttons()
        for button in Button.get_buttons():
            if isinstance(buttons[button], CircleButton):
                if mouse - buttons[button].pos < buttons[button].radius:
                    buttons[button].is_hover = True
                    if PygameUtils.is_mouse_pressed(0):
                        buttons[button].is_pressed = True
                    else:
                        buttons[button].is_pressed = False
                else:
                    buttons[button].is_pressed = False