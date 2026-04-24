from Utils.Buttons.CircleButton import CircleButton
from Utils.Buttons.SquareButton import SquareButton
from Utils.PygameUtils import PygameUtils


class Utils:
    @staticmethod
    def update():
        PygameUtils.update()
        SquareButton.update()
        CircleButton.update()

    @staticmethod
    def draw(window):
        SquareButton.draw(window)
        CircleButton.draw(window)

    @staticmethod
    def add_button(name, kind, pos, color, width=None, height=None, hover_color=None, press_color=None, radius=0): #kind = "Circle" or kind = "Square"
        if kind == "Square":
            SquareButton(name, pos, width, height, color, hover_color=hover_color, press_color=press_color, radius=radius)
        elif kind == "Circle":
            CircleButton(name, pos, radius, color, hover_color=hover_color, press_color=press_color)