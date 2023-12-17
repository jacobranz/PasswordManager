from models.main import Model
from models.auth import User, Password
from views.main import View


class LoginController:
    def __init__(self, model: Model, view: View) -> None:
        self.model = model
        self.view = view
        self.frame = self.view.frames["login"]
        self._bind()

    def _bind(self) -> None:
        """Binds controller functions with respective buttons in the view"""
        self.frame.login_button.configure(command=self.signin)
        self.frame.signup_btn.configure(command=self.signup)

    def signup(self) -> None:
        self.view.switch("signup")

    def signin(self) -> None:
        username = self.frame.username_entry.get()
        user_pasword = self.frame.password_entry.get()
        data = {"username": username, "password": user_pasword}
        print(data)
        self.frame.password_entry.delete(0, len(user_pasword))
        user: User = {"username": data["username"]}
        password: Password = {"password": data["password"]}
        self.model.auth.login(user, password)