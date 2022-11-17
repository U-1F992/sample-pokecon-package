from Commands.PythonCommandBase import PythonCommand
from Commands.Keys import Button


def press_a(command: PythonCommand):
    command.press(Button.A)
