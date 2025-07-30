from PySide6.QtCore import QObject, Signal, Slot
from PySide6.QtWidgets import QWidget

from resources.widget import Ui_Form


class EventSender(QObject):
    signal = Signal(str)
    @Slot()

    def send_signal(self,):
        self.signal.emit(1)

class GlobalData:

    def __init__(self):
        self.sender = EventSender()
        self.i=0
        pass

    def __setattr__(self, name, value):
        super().__setattr__(name, value)
        self.sender.send_signal()


class Widget(Ui_Form, QWidget, ):

    def __init__(
            self,
            parent=None,
            global_data:GlobalData=None,
        ) -> None:
        QWidget.__init__(self)
        self.setupUi(self)
        self.module_starter_button.clicked.connect(self.push_data)
        self.setParent(parent)
        self.global_data=global_data
        self.label.setText(f'self.global_data.i {self.global_data.i}')
        self.global_data.sender.signal.connect(self.update_i)

    def push_data(self):
        self.global_data.i+=1
        self.parent().label.setText(f'опа опа и опа! {self.global_data.i}')

    def update_i(self):
        self.label.setText(f'self.global_data.i {self.global_data.i}')