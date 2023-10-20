from vsdlib.board import Board, BoardLayout, SubLayout
from vsdlib.buttons import Button
from vsdlib.button_style import ButtonStyle
from vsdlib.widgets import KeyPadWidget
from vsdlib.colors import grays

from .utils import get_asset_path

from pynput.keyboard import Controller

keyboard = Controller()


def create_push_button(button:str):
    def push_button(pressed:bool):
        if not pressed:
            return
        keyboard.type(button)
    return push_button


class EliteDangerousWidget(KeyPadWidget):
    #TODO:merge to a number_buttons list and index by the number you want, e.g. number_buttons[0] will be the 0 button.
    bplus: Button
    bminus: Button
    bequals: Button
    bmult: Button
    bdiv: Button
    bbackspace: Button
    result_style = ButtonStyle(background_color='#37d495', pressed_background_color='#297858')
    def __init__(self, board:Board, style:ButtonStyle=ButtonStyle()):
        # super().__init__(board, self.result_style)
        super().__init__(board, style)

        self.shield = Button(create_push_button('.'), text='Shield')
        self.thing2 = Button(create_push_button('('), text='Thing2')
        self.thing3 = Button(create_push_button(')'), text='Thing3')


class EliteDangerousLayout(SubLayout):
    edwidget: EliteDangerousWidget
    def __init__(self, board:Board, from_layout:BoardLayout):
        super().__init__(
            "Calc", board, from_layout,
            button_style=ButtonStyle(image_path=get_asset_path('calculator.jpg')),
        )
        self.edwidget = EliteDangerousWidget(board)
        buttons = [
            self.edwidget.shield,
            self.edwidget.thing2,
            self.edwidget.thing3,
        ]
        for i, button in enumerate(buttons):
            self.layout.set(button, i)
