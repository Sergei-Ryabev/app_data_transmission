from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow

from resources.main_window import Ui_MainWindow
from services.widget import GlobalData, Widget

Window=Qt.WindowType.Window


class MainWindow(Ui_MainWindow, QMainWindow, ):
    def __init__(self) -> None:
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.module_starter_button.clicked.connect(self.open_wiget)
        self.widgets = []
        self.global_data=GlobalData()

    def open_wiget(self):
        wiget=Widget(parent=self, global_data=self.global_data)
        wiget.setWindowFlag(Window)
        wiget.show()
        self.widgets.append(wiget)
