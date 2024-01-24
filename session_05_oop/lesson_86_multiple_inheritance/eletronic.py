from log import logMixin

class Eletronic(logMixin):
    def __init__(self, name):
        self._name = name
        self._switched_on = False

    def turn_on(self):
        if self._switched_on:
            error = f"{self._name} is already on"
            print(error)
            self.log_error(error)
            return
        else:
            info = f'{self._name} was turned on'
            print(info)
            self.log_info(info)
            self._switched_on = True

    def turn_off(self):
        if not self._switched_on:
            error = f"{self._name} isn't on"
            print(error)
            self.log_error(error)
            return
        else:
            info = f'{self._name} has been turned off'
            print(info)
            self.log_info(info)
            self._switched_on = False
