from machine import Pin, Timer


class Button:
    DEBOUNCE_TIME = 50

    def __init__(self, pin_number, handler_function=None):
        self.pin = Pin(pin_number, Pin.IN)
        self.timer = Timer(0)
        self.handlerFunction = handler_function


    def get_value(self):
        return self.pin.value()
    
    def is_pressed(self):
        return self.get_value() == 0
    
    def add_event():
        pass

    def add_event(self, handler, trigger=Pin.IRQ_FALLING):
        self.pin.irq(handler=self.button_pressed, trigger=trigger)
    
    def debounce(self, timer):
        if self.is_pressed():
            self.handler_function()

    def button_pressed(self, pin):
        self.timer.deinit()
        self.timer.init(mode=Timer.ONE_SHOT, period=100, callback=self.debounce)
