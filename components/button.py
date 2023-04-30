from machine import Pin, Timer


class Button:

    def __init__(self, pin_number):
        self.pin = Pin(pin_number, Pin.IN)
        self.timer = Timer(0)
        self.handler_function = None

    def get_value(self):
        return self.pin.value()

    def is_pressed(self):
        return self.get_value() == 0

    def add_event(self, handler_function, trigger=Pin.IRQ_RISING):
        self.handler_function = handler_function
        self.pin.irq(handler=self.debounce, trigger=trigger)

    def debounce(self, pin):
        self.timer.deinit()
        self.timer.init(mode=Timer.ONE_SHOT, period=200,
                        callback=self.button_pressed)

    def button_pressed(self, pin):
        self.handler_function()
