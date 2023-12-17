from .auth import Auth
from .database import database_commands


class Model:
    def __init__(self):
        self.auth = Auth()
        self.db_commands = database_commands