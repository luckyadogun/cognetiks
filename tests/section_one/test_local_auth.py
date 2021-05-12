import random

import pytest

from src.section_one.local_auth import LocalAuth


class TestLocalAuth:
    def test_auth_system_exists(self):
        """
        GIVEN a class named LocalAuth
        WHEN globals() is checked for its existence
        THEN LocalAuth must exist in the global namespace
        """
        assert "LocalAuth" in globals()

    def test_auth_has_attributes_username_and_password(
        self, users
    ):
        """
        GIVEN a class named LocalAuth
        WHEN hasattr(instance, 'attribute') is checked
        THEN the response == True
        """
        username, password = random.choice(
            list(users.items())
        )
        auth = LocalAuth(
            username=username, password=password
        )

        assert hasattr(auth, "username")
        assert hasattr(auth, "password")

    def test_store_users(self, users):
        """
        GIVEN a username and password
        WHEN create account is called
        THEN the user is saved to storage as username/pwd pair
        """
        username, password = random.choice(
            list(users.items())
        )

        auth = LocalAuth(
            username=username, password=password
        )
        user = auth.store()

        assert user == "Successfully stored!"
