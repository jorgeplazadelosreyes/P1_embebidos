from machine import Pin
import utime

class LoadCell:
    def __init__(self, dt_pin_numb, sck_pin_numb, calibration_factors=[2008.8, -58100]):
        self.dt_pin = Pin(dt_pin_numb, Pin.IN)
        self.scl_pin = Pin(sck_pin_numb, Pin.OUT)
        self.calibration_factors = calibration_factors

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

        weight = (float((data ^ 0x800000) - 0x800000) - self.calibration_factors[1]) / self.calibration_factors[0]

        return weight
    


