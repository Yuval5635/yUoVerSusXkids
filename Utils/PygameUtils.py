import pygame as pg
from Utils.Vector import Vector

class PygameUtils:
    __keys = None
    __old_keys = None
    __events = []
    __mouse_position = None
    __mouse_buttons = None
    __mouse_old_buttons = None

    @staticmethod
    def update():
        PygameUtils.old_keys = PygameUtils.keys
        PygameUtils.keys = pg.key.get_pressed()
        PygameUtils.events = pg.event.get()
        PygameUtils.mouse_position = Vector(pg.mouse.get_pos()[0], pg.mouse.get_pos()[1])
        PygameUtils.mouse_old_buttons_buttons = PygameUtils.mouse_buttons
        PygameUtils.mouse_buttons = pg.mouse.get_pressed()

    @staticmethod
    def is_key_held(key):
        return PygameUtils.__keys[key]

    @staticmethod
    def is_key_pressed(key):
        return PygameUtils.__keys[key] and not PygameUtils.__old_keys[key]

    @staticmethod
    def get_mouse_position():
        return PygameUtils.__mouse_position

    @staticmethod
    def is_mouse_held(button):
        return PygameUtils.__mouse_buttons[button]

    @staticmethod
    def is_mouse_pressed(button): #0 - Left, 1 - Middle, 2 - Right
        return PygameUtils.__mouse_buttons[button] and not PygameUtils.__mouse_old_buttons[button]