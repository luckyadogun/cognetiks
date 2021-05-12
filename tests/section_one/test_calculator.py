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
