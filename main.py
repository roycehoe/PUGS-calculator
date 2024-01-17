from enum import Enum, auto

MENU_INTRODUCTION = "Hi there! Thank you for using my calculator app"
MENU_EXIT = "Goodbye"

PROMPT_MENU_SELECTION = """
Please select from one of the following options by inputting the corresponding number

[1] - Begin
[0] - Exit
"""
PROMPT_MENU_INVALID_INPUT = "You have entered an invalid number. Please try again"

PROMPT_MATHEMATICAL_OPERATION = """
Please select your mathematical operation by inputing the corresponding number

[1] - Addition
[2] - Subtraction
[3] - Multiplication
[4] - Division
"""
PROMPT_FIRST_NUMERICAL_CONSTANT = "Please input your first number"
PROMPT_SECOND_NUMERICAL_CONSTANT = "Please input your second number"
PROMPT_INVALID_NUMBER = "You have entered an invalid number. Please try again"


class MenuSelection(Enum):
    BEGIN = auto()
    EXIT = auto()


class MathematicalOperation(Enum):
    ADDITION = auto()
    SUBTRACTION = auto()
    MULTIPLICATION = auto()
    DIVISION = auto()


class InvalidMenuSelectionError(Exception):
    pass


class InvalidMathematicalOperationError(Exception):
    pass


class InvalidNumericalConstantError(Exception):
    pass

def get_menu_selection(menu_input: str) -> MenuSelection:
    if menu_input == "1":
        return MenuSelection.BEGIN
    if menu_input == "0":
        return MenuSelection.EXIT
    raise InvalidMenuSelectionError



def get_menu_input() -> MenuSelection:
    while True:
        try:
            menu_selection = input(PROMPT_MENU_SELECTION)
            menu_input = get_menu_selection(menu_selection)
            return menu_input
        except InvalidMenuSelectionError:
            print(PROMPT_MENU_INVALID_INPUT)

print(MENU_INTRODUCTION)
menu_input = get_menu_input()