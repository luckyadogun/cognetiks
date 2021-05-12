import pytest

class TestLocalAuth:
    def test_auth_system_exists(self):
        """
        GIVEN a class named LocalAuth
        WHEN globals() is checked for its existence
        THEN LocalAuth must exist in the global namespace
        """
        assert "LocalAuth" in globals()