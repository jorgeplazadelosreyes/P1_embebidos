from machine import Pin, Timer


class InfraRed:
    DEBOUNCE_TIME = 50

    def __init__(self, pin_number):
        self.pin = Pin(pin_number, Pin.IN)
        self.last_state = self.get_value()
        self.timer = Timer(0)
        self.handler_function = None
        

    def get_value(self):
        return self.pin.value()
    
    def detect(self):
        return self.get_value() == 0
    
    def add_event(self, handler_function, trigger=Pin.IRQ_FALLING):
        self.handler_function = handler_function
        self.pin.irq(handler=self.state_changed, trigger=trigger)

    def state_changed(self, pin):
        self.timer.deinit()
        self.timer.init(mode=Timer.ONE_SHOT, period=100, callback=self.debounce)

    def debounce(self, timer):
        self.handler_function()   