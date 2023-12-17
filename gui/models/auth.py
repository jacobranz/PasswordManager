from typing import TypedDict, Union
from .base import ObservableModel
from .database import database_connection, database_commands

class User(TypedDict):
    username: str

class Password(TypedDict):
    password: str


class Auth(ObservableModel):
    def __init__(self):
        super().__init__()
        self.is_logged_in = False
        self.current_user: Union[User, None] = None

    def login(self, user: User, password: Password) -> None:
        self.current_user = user
        self.current_password = password
        try:
            database_commands.queryUser(self.current_user)
            database_commands.queryPass(self.current_user, self.current_password)
            self.is_logged_in = True
        except:
            ValueError("Incorrect objects entered into string fields.")

        self.trigger_event("auth_changed")

    def logout(self) -> None:
        self.is_logged_in = False
        self.current_user = None
        self.trigger_event("auth_changed")