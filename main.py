from enum import Enum, auto

DISPLAY_MENU_BANNER = """
--------------------------------
|          CALCULATOR           |
--------------------------------
"""
DISPLAY_MENU_INTRODUCTION = "Hi there! Thank you for using my calculator app"
DISPLAY_MENU_EXIT = "Goodbye"
DISPLAY_CALCULATOR_ERROR = "Hmm, something went wrong. Let us try this again"
DISPLAY_CALCULATOR_RESULT = "Ans:"

PROMPT_MENU_SELECTION = """
Please select from one of the following options by inputting the corresponding number

[1] - Begin
[0] - Exit
"""
PROMPT_INVALID_INPUT = "You have entered an invalid number. Please try again"

PROMPT_MATHEMATICAL_OPERATION = """
Please select your mathematical operation by inputing the corresponding number

[1] - Addition
[2] - Subtraction
[3] - Multiplication
[4] - Division
"""
PROMPT_FIRST_NUMERICAL_CONSTANT = "Please input your first number: "
PROMPT_SECOND_NUMERICAL_CONSTANT = "Please input your second number: "
PROMPT_INVALID_NUMBER = "You have entered an invalid number. Please try again"

PROMPT_USE_CALCULATOR_AGAIN = """
Please select from one of the following options by inputting the corresponding number

[1] - Begin
[0] - Exit
"""


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


class InvalidCalculatorResultError(Exception):
    pass


def _get_menu_selection(menu_input: str) -> MenuSelection:
    if menu_input == "1":
        return MenuSelection.BEGIN
    if menu_input == "0":
        return MenuSelection.EXIT
    raise InvalidMenuSelectionError


def get_menu_input() -> MenuSelection:
    while True:
        try:
            menu_selection = input(PROMPT_MENU_SELECTION)
            menu_input = _get_menu_selection(menu_selection)
            return menu_input
        except InvalidMenuSelectionError:
            print(PROMPT_INVALID_INPUT)


def _get_mathematical_selection(
    mathematical_operation_input: str,
) -> MathematicalOperation:
    if mathematical_operation_input == "1":
        return MathematicalOperation.ADDITION
    if mathematical_operation_input == "2":
        return MathematicalOperation.SUBTRACTION
    if mathematical_operation_input == "3":
        return MathematicalOperation.MULTIPLICATION
    if mathematical_operation_input == "4":
        return MathematicalOperation.DIVISION
    raise InvalidMathematicalOperationError


def get_mathematial_operation_input() -> MathematicalOperation:
    while True:
        try:
            mathematical_operation_selection = input(PROMPT_MATHEMATICAL_OPERATION)
            mathematical_operation_input = _get_mathematical_selection(
                mathematical_operation_selection
            )
            return mathematical_operation_input
        except InvalidMenuSelectionError:
            print(PROMPT_INVALID_INPUT)


def get_numerical_constant(prompt: str) -> int:
    try:
        numerical_constant = int(input(prompt))
        return numerical_constant
    except TypeError:
        raise InvalidNumericalConstantError


def compute_calculator_result(
    mathematical_operation: MathematicalOperation,
    first_numerical_constant: int,
    second_numerical_constant: int,
) -> float:
    try:
        if mathematical_operation == MathematicalOperation.ADDITION:
            return first_numerical_constant + second_numerical_constant
        if mathematical_operation == MathematicalOperation.SUBTRACTION:
            return first_numerical_constant - second_numerical_constant
        if mathematical_operation == MathematicalOperation.MULTIPLICATION:
            return first_numerical_constant * second_numerical_constant
        if mathematical_operation == MathematicalOperation.DIVISION:
            return first_numerical_constant / second_numerical_constant
    except ZeroDivisionError:
        raise InvalidCalculatorResultError


def get_calculator_result() -> float:
    while True:
        try:
            mathematical_operation = get_mathematial_operation_input()
            first_numerical_constant = get_numerical_constant(
                PROMPT_FIRST_NUMERICAL_CONSTANT
            )
            second_numerical_constant = get_numerical_constant(
                PROMPT_SECOND_NUMERICAL_CONSTANT
            )
            calculator_result = compute_calculator_result(
                mathematical_operation,
                first_numerical_constant,
                second_numerical_constant,
            )
            return calculator_result
        except InvalidCalculatorResultError:
            print(f"{DISPLAY_CALCULATOR_ERROR} \n")


while True:
    print(DISPLAY_MENU_BANNER)
    print(DISPLAY_MENU_INTRODUCTION)
    menu_input = get_menu_input()
    if menu_input == MenuSelection.EXIT:
        print(DISPLAY_MENU_EXIT)
        exit()
    calculator_result = get_calculator_result()
    print(f"{DISPLAY_CALCULATOR_RESULT}: {calculator_result}")
