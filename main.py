# main.py -- put your code here!
from components.button import Button
from components.infraRed import InfraRed
from components.lcdI2c import LcdI2c
from components.servo import Servo
from components.loadCell import LoadCell
from components.led import Led
from machine import Pin, I2C, SoftI2C


import time


#Dirección del I2C y tamaño del LCD

def main():  
    lcd = LcdI2c(sda_pin_numb=4, scl_pin_numb=5)
    infraRed = InfraRed(pin_number=25)
    redLed = Led(pin_number=26)
    greenLed = Led(pin_number=15)
    servo = Servo(pin_number=14)

    while True:
        if infraRed.get_value() == 1:
            redLed.turn_on()
            greenLed.turn_off()
            servo.move(180)
            time.sleep(1)
        else:
            redLed.turn_off()
            greenLed.turn_on()
            servo.move(0)
            time.sleep(1)

        time.sleep(0.1)



if __name__ == '__main__':
    main()



