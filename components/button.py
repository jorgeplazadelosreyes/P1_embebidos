from machine import Pin

class Button:

    def __init__(self, pin_number):
        self.pin = Pin(pin_number, Pin.IN)

    def get_value(self):
        return self.pin.value()