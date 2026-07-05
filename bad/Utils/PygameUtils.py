import pygame as pg

class PygameUtils:
    keys = None
    old_keys = None
    events = []

    @staticmethod
    def update():
        PygameUtils.old_keys = PygameUtils.keys
        PygameUtils.keys = pg.key.get_pressed()
        PygameUtils.events = pg.event.get()

    @staticmethod
    def is_key_held(key):
        return PygameUtils.keys[key]

    @staticmethod
    def is_key_pressed(key):
        return PygameUtils.keys[key] and not PygameUtils.old_keys[key]