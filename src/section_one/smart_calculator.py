import operator as math_operator


class OperatorError(Exception):
    pass


class OperandError(Exception):
    pass


ARITHEMETIC_KEYS = {
    "maths": {
        "+": math_operator.add,
        "-": math_operator.sub,
        "*": math_operator.mul,
        "/": math_operator.truediv,
    },
    "english": {
        "add": math_operator.add,
        "subtract": math_operator.sub,
        "multiply": math_operator.mul,
        "divide": math_operator.truediv,
    },
}


def calculate(
    operand_1: int,
    operand_2: int,
    operator: str,
    math_func=ARITHEMETIC_KEYS,
):

    if not isinstance(operand_1, int) and not isinstance(
        operand_2, int
    ):
        raise OperandError(
            "<operands> can only be integer values"
        )

    if not isinstance(operator, str):
        raise OperatorError(
            "<operator> can only be in mathematical string representations eg: '+' or 'add'"
        )

    if operator in math_func["maths"]:
        return math_func["maths"][operator](
            operand_1, operand_2
        )
    elif operator in math_func["english"]:
        return math_func["english"][operator](
            operand_1, operand_2
        )
    else:
        raise OperatorError(
            """
            Invalid operator keys. Try:
                - '+" or 'add'
                - '-' or 'subtract'
                - '/' or 'divide'
                - '*' or 'multiply'
            """
        )
