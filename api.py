from enum import Enum, auto

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class MathematicalOperation(Enum):
    ADDITION = auto()
    SUBTRACTION = auto()
    MULTIPLICATION = auto()
    DIVISION = auto()


class CalculatorRequest(BaseModel):
    first_numerical_constant: float
    second_numerical_constant: float
    mathematical_operation: MathematicalOperation


class CalculatorResponse(BaseModel):
    result: float


class InvalidMathematicalOperationError(Exception):
    pass


def get_calculator_answer(calculator_request: CalculatorRequest):
    try:
        if calculator_request.mathematical_operation == MathematicalOperation.ADDITION:
            return (
                calculator_request.first_numerical_constant
                + calculator_request.second_numerical_constant
            )
        if (
            calculator_request.mathematical_operation
            == MathematicalOperation.SUBTRACTION
        ):
            return (
                calculator_request.first_numerical_constant
                - calculator_request.second_numerical_constant
            )
        if (
            calculator_request.mathematical_operation
            == MathematicalOperation.MULTIPLICATION
        ):
            return (
                calculator_request.first_numerical_constant
                * calculator_request.second_numerical_constant
            )
        if calculator_request.mathematical_operation == MathematicalOperation.DIVISION:
            return (
                calculator_request.first_numerical_constant
                / calculator_request.second_numerical_constant
            )
        raise InvalidMathematicalOperationError
    except ZeroDivisionError:
        raise ZeroDivisionError


def get_calculator_response(
    calculator_request: CalculatorRequest,
) -> CalculatorResponse:
    try:
        calculator_answer = get_calculator_answer(calculator_request)
        return CalculatorResponse(result=calculator_answer)
    except InvalidMathematicalOperationError:
        raise InvalidMathematicalOperationError
    except ZeroDivisionError:
        raise ZeroDivisionError


@app.post("/")
def calculator(request: CalculatorRequest) -> CalculatorResponse:
    try:
        return get_calculator_response(request)
    except InvalidMathematicalOperationError:
        raise HTTPException(status_code=400, detail="Invalid mathematical operation")
    except ZeroDivisionError:
        raise HTTPException(status_code=400, detail="Zero division error")
