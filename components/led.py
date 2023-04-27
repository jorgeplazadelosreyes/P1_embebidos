from machine import Pin

class Led:
    def __init__(self, pin_number):
        self.__led = Pin(pin_number, Pin.OUT)

    def turn_on(self):
        self.__led.value(1)

    def turn_off(self):
        self.__led.value(0)
