from machine import Pin
import utime

class LoadCell:
    def __init__(self, dt_pin_num, sck_pin_num, calibration_factor=1):
        self.dt_pin = Pin(dt_pin_num, Pin.IN)
        self.scl_pin = Pin(sck_pin_num, Pin.OUT)

    def get_value(self):
        while self.dt_pin.value() == 1:
            pass

        data = 0

        for i in range(24):
            self.scl_pin.on()
            utime.sleep_us(1)
            data <<= 1
            self.scl_pin.off()
            utime.sleep_us(1)
            data |= self.dt_pin.value()

        self.scl_pin.on()
        self.scl_pin.off()

        weight = float((data ^ 0x800000) - 0x800000) / self.calibration_factor

        return weight
