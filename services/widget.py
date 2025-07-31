
from PySide6.QtWidgets import QWidget

from resources.widget import Ui_Form
from .source import Basis, ChangeEvent
from PySide6.QtCore import QObject, Signal, Slot


class Widget(Ui_Form, QWidget, Basis ):

    def __init__(
            self,
            parent=None,
        ) -> None:
        QWidget.__init__(self)
        self.setupUi(self)
        self.module_starter_button.clicked.connect(self.push_data)
        self.setParent(parent)
        self.label.setText(f'self.global_data.i {self.global_data.i}')
        self.global_data._sender.signal.connect(self.update_i)

    def push_data(self):
        self.global_data.i+=1
        self.parent().label.setText(f'опа опа и опа! {self.global_data.i}')

    @Slot(ChangeEvent)
    def update_i(self, data:ChangeEvent):
        self.label.setText(f'Приняли синал от {data.attr_name} значение стало {data.new_value}')