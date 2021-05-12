class OperatorError(Exception):
    pass


class OperandError(Exception):
    pass


def calculate(
    operand_1: int, operand_2: int, operator: str
):
    if not isinstance(operand_1, int) and not isinstance(
        operand_2, int
    ):
        raise OperandError(
            "<operands> can only be integer values"
        )
