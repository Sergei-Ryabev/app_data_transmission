from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow

from resources.main_window import Ui_MainWindow
from services.widget import Widget
from .source import Basis

Window=Qt.WindowType.Window


class MainWindow(Ui_MainWindow, QMainWindow, ):
    def __init__(self) -> None:
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.module_starter_button.clicked.connect(self.open_wiget)
        self.widgets = []
        

    def open_wiget(self):
        wiget=Widget(parent=self)
        wiget.setWindowFlag(Window)
        wiget.show()
        self.widgets.append(wiget)
