import json


class UserAlreadyExistsError(Exception):
    pass


class UserDoesNotExistsError(Exception):
    pass


class LocalStorageDB:
    def __init__(self) -> None:
        self.store = "text_db.txt"

    def _read(self):
        with open(self.store, "r") as f:
            data = json.loads(f.read())

        return data

    def _write(self, username, password):
        with open(self.store, "a+") as f:
            old = self._read()
            new = old[username] = password
            data = json.dumps(f.write(new))

        return data

    def save(self, username, password):
        user = self._write(username, password)
        if username in self._read():
            return "Successfully stored!"

    def user_exists(self, username):
        if username in self._read():
            return True
        return False

    def _encrypt(self):
        pass

    def _decrypt(self):
        pass


class LocalAuth:
    def __init__(
        self, username: str, password: str
    ) -> None:
        self.username = username
        self.password = password
        self.db = LocalStorageDB()

    def is_authenticated(self) -> bool:
        if self.db.user_exists(self.username):
            return True
        return False

    def store(self):
        return self.db.save(self.username, self.password)
