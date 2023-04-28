from util.dispenser import Dispenser
from machine import Pin

def button1_handler(pin, lcd):
    lcd.print("Hola mundo", wait=1, clear=True)
    print("Hola mundo")

class Program:

    def __init__(self):
        self.dispenser = Dispenser()

    def run(self):
        pass