from PySide6.QtCore import Qt, Slot
from PySide6.QtWidgets import QMainWindow

from resources.main_window import Ui_MainWindow
from services.widget import Widget

from .source import Basis, ChangeEvent

Window=Qt.WindowType.Window


class MainWindow(Ui_MainWindow, QMainWindow, Basis):
    def __init__(self) -> None:
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.module_starter_button.clicked.connect(self.open_wiget)
        self.widgets = []
        self.global_data.update_signal.connect(self.update_gd)

    @Slot(ChangeEvent)    
    def update_gd(self,data:ChangeEvent):
        self.input_line.setText(f'{data.attr_name}')
        
    def open_wiget(self):
        wiget=Widget(parent=self)
        wiget.setWindowFlag(Window)
        wiget.show()
        self.widgets.append(wiget)
