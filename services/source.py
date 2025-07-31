from typing import Any

from PySide6.QtCore import QObject, Signal, Slot


class ChangeEvent:
    def __init__(self, attr_name: str, old_value: Any, new_value: Any):
        self.attr_name = attr_name
        self.old_value = old_value
        self.new_value = new_value


class GlobalData(QObject):
    update_signal = Signal(ChangeEvent)

    @Slot(ChangeEvent)
    def send_signal(self,change_event:ChangeEvent):
        self.update_signal.emit(change_event)

    def __init__(self):
        super().__init__()
        self.i=0

    def __setattr__(self, name, value):
        if name.startswith('_'):
            super().__setattr__(name, value)
        else:
            old_value = self.__dict__.get(name, None)
            self.__dict__[name] = value
            event = ChangeEvent(
                        attr_name=name,
                        old_value=old_value,
                        new_value=value
            )
            self.send_signal(event)

class Basis:
    global_data=GlobalData()