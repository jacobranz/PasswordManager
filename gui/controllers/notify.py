from models.main import Model
from views.main import View

class NotifyController():
    def __init__(self, model: Model, view: View) -> None:
        self.model = model
        self.view = view
        self.view.frames["nofify"]
        self._bind()

    def _bind(self) -> None:
        """Binds controller functions with respective buttons in the view"""
        self.frame.close_button.configure(command=self.close)

    def close(self) -> None:
        # Close CTK Frame
        self.frame.destroy()