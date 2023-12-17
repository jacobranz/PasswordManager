from typing import TypedDict

from .root import PassMan
from .home import HomeView
from .login import LoginPage
from .signup import SignUp
from .notify import Notify

class Frames(TypedDict):
    login: LoginPage
    SignUp: SignUp
    home: HomeView
    nofify: Notify

class View:
    def __init__(self):
        self.root = PassMan()
        self.frames: Frames = {}

        self._add_frame(SignUp, "signup")
        self._add_frame(LoginPage, "login")
        self._add_frame(HomeView, "home")
        self._add_frame(Notify, "notify")

    def _add_frame(self, Frame, name: str) -> None:
        self.frames[name] = Frame(self.root)
        self.frames[name].grid(row=0, column=0, sticky="nsew")

    def switch(self, name: str) -> None:
        frame = self.frames[name]
        frame.tkraise()

    def start_mainloop(self) -> None:
        self.root.mainloop()