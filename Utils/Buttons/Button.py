class Button:
    __all_buttons = {}

    def __init__(self, name, pos, color, hover_color=None, press_color=None):
        if hover_color is None:
            hover_color = color
        if press_color is None:
            press_color = color
        self.pos = pos
        self.color = color
        self.hover_color = hover_color
        self.press_color = press_color
        self.is_pressed = False
        self.is_hover = False
        Button.__all_buttons[name] = self

    @staticmethod
    def get_buttons():
        return Button.__all_buttons