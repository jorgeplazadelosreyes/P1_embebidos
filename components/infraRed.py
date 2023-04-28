from machine import Pin, Timer

class InfraRed:

    def __init__(self, pin_number, leds=None):
        self.pin = Pin(pin_number, Pin.IN)
        self.last_state = self.get_value()
        self.leds = leds
        self.timer = Timer(0)
        
        self.add_event()

    def get_value(self):
        return self.pin.value()
    
    def detect(self):
        return self.get_value() == 0
    

    def add_event(self, trigger=Pin.IRQ_FALLING):
        self.pin.irq(handler=self.state_changed, trigger=trigger)

    def state_changed(self, pin):
        self.timer.deinit()
        self.timer.init(mode=Timer.ONE_SHOT, period=100, callback=self.debounce)

    def debounce(self, timer):
        if self.detect():
            self.leds["green"].turn_on()
            self.leds["red"].turn_off()
        else:
            self.leds["green"].turn_off()
            self.leds["red"].turn_on()


    
