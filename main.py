from enum import Enum, auto

MENU_INTRODUCTION = "Hi there! Thank you for using my calculator app"
MENU_EXIT = "Goodbye"

PROMPT_MENU_SELECTION = """
Please select from one of the following options by inputting the corresponding number

[1] - Begin
[2] - Exit
"""
PROMPT_MENU_INVALID_INPUT = "You have entered an invalid number. Please try again"

PROMPT_FIRST_NUMERICAL_CONSTANT = "Please input your first number"
PROMPT_SECOND_NUMERICAL_CONSTANT = "Please input your second number"
PROMPT_MATHEMATICAL_OPERATION = """
Please select your mathematical operation by inputing the corresponding number

[1] - Addition
[2] - Subtraction
[3] - Multiplication
[4] - Division
"""
PROMPT_INVALID_NUMBER = "You have entered an invalid number. Please try again"


class MathematicalOperation(Enum):
    ADDITION = auto()
    SUBTRACTION = auto()
    MULTIPLICATION = auto()
    DIVISION = auto()


class InvalidIntroductionInputError(Exception):
    pass


class InvalidMathematicalOperationError(Exception):
    pass


class InvalidNumericalConstantError(Exception):
    pass


print(MENU_INTRODUCTION)
introduction_input = input(PROMPT_MENU_SELECTION)
