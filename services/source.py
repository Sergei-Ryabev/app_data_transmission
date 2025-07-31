from PySide6.QtCore import QObject, Signal, Slot
from typing import Any


class ChangeEvent:
    def __init__(self, attr_name: str, old_value: Any, new_value: Any):
        self.attr_name = attr_name
        self.old_value = old_value
        self.new_value = new_value

class EventSender(QObject):

    signal = Signal(ChangeEvent)
    @Slot(ChangeEvent)
    def send_signal(self,change_event:ChangeEvent):
        self.signal.emit(change_event)


class GlobalData():
    signal = Signal(str)

    def __init__(self):
        self._sender = EventSender()
        self.i=0
        pass

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
            self._sender.send_signal(event)

class Basis:
    global_data=GlobalData()