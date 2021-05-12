import pytest

from src.section_one.smart_calculator import (
    calculate,
    OperandError,
    OperatorError,
)


class TestCalculator:
    def test_calculator_function_exists(self):
        """
        GIVEN a function called calculate
        WHEN globals() is checked for its existence
        THEN calculate must exist in the global namespace
        """
        assert "calculate" in globals()

    def test_calculator_can_only_accept_integer_operands(
        self,
    ):
        """
        GIVEN a non-integer operand values
        WHEN calculate function is called
        THEN an exception is raised with specific message
        """
        with pytest.raises(OperandError) as exc:
            calculate("a", "b", "add")

        assert (
            str(exc.value)
            == "<operands> can only be integer values"
        )

    def test_calculator_can_only_accept_math_string_operators(
        self,
    ):
        """
        GIVEN a non-string or non-math string operator value
        WHEN calculate function is called
        THEN an exception is raised with specific message
        """
        with pytest.raises(
            OperatorError
        ) as exc_invalid_opr:
            calculate(1, 2, True)

        with pytest.raises(
            OperatorError
        ) as exc_invalid_key:
            calculate(1, 2, "adds")

        assert (
            str(exc_invalid_opr.value)
            == "<operator> can only be in mathematical string representations eg: '+' or 'add'"
        )

        assert (
            str(exc_invalid_key.value)
            == """
            Invalid operator keys. Try:
                - '+" or 'add'
                - '-' or 'subtract'
                - '/' or 'divide'
                - '*' or 'multiply'
            """
        )

    def test_simple_math_funcs_work(self):
        """
        GIVEN a correct operator and integer operands
        WHEN calculate function is called
        THEN the expected output is returned
        """
        assert calculate(2, 2, "+") == 4
        assert calculate(2, 2, "add") == 4

        assert calculate(2, 8, "multiply") == 16
        assert calculate(2, 8, "*") == 16

        assert calculate(2, 10, "-") == -8
        assert calculate(10, 2, "subtract") == 8

        assert calculate(2, 20, "/") == 0.1
        assert calculate(20, 2, "divide") == 10
