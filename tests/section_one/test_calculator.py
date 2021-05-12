import pytest

from src.section_one.smart_calculator import calculate


class TestCalculator:
    def test_calculator_function_exists(self):
        """
        GIVEN a function called calculate
        WHEN globals() is checked for its existence
        THEN calculate must exist in the global namespace
        """
        assert "calculate" in globals()