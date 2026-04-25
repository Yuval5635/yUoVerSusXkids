from Utils.Buttons.Button import Button
import pygame as pg

from Utils.PygameUtils import PygameUtils


class CircleButton(Button):
    def __init__(self, name, pos, radius, color, hover_color=None, press_color=None):
        super().__init__(name, pos, color, hover_color, press_color)
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
            pg.draw.circle(window, color, (button.pos.x, button.pos.y), button.radius)

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