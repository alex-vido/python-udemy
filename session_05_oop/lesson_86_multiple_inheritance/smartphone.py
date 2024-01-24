from eletronic import Eletronic
from log import logMixin

class Smartphone(Eletronic, logMixin):
    def __init__(self, name):
        super().__init__(name)
        self._connected = False

    def connect(self):
        if not self._switched_on:
            error = f"{self._name} isn't turned on"
            print(error)
            self.log_error(error)
            return

        if self._connected:
            error = f'{self._name} is already connected'
            print(error)
            self.log_error(error)
            return
        info = f'{self._name} is connected'
        print(info)
        self.log_info(info)
        self._connected = True

    def disconnect(self):
        if not self._connected:
            error = f"{self._name} isn't connected"
            print(error)
            self.log_error(error)
            return

        info = f'{self._name} is disconnected'
        print(info)
        self.log_info(info)
        self._connected = False
