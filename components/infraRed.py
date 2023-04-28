from machine import Pin

class InfraRed:

    def __init__(self, pin_number):
        self.pin = Pin(pin_number, Pin.IN)

    def get_value(self):
        return self.pin.value()
    
    def detect(self):
        return self.get_value() == 1