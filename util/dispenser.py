from components.button import Button
from components.infraRed import InfraRed
from components.lcdI2c import LcdI2c
from components.servo import Servo
from components.loadCell import LoadCell
from components.led import Led
from time import time, sleep, sleep_ms
from machine import Pin, Timer

class DriedFruit:
    def __init__(self, name, amount, time):
        self.name = name
        self.amount = amount
        self.time = time

class Dispenser:
    PENAUT_AMOUNT = 50
    ALMOND_AMOUNT = 100
    WALNUT_AMOUNT = 80

    PENAUT_TIME = 0.5
    ALMOND_TIME = 0.5
    WALNUT_TIME = 0.5

    SERVO_PIN_NUMBER = 14
    LCD_SDA_PIN_NUMBER = 4
    LCD_SCL_PIN_NUMBER = 5
    LOAD_CELL_DT_PIN_NUMBER = 33
    LOAD_CELL_SCK_PIN_NUMBER = 32
    INFRA_RED_CUP_PIN_NUMBER = 23
    INFRA_RED_LOAD_PIN_NUMBER = 25
    RED_LED_PIN_NUMBER = 26
    GREEN_LED_PIN_NUMBER = 15
    BUTTON_OPTION_PIN_NUMBER = 19
    BUTTON_ACTION_PIN_NUMBER = 2


    def __init__(self):
        self.dried_fruits = [
            DriedFruit("peanut", self.PENAUT_AMOUNT, self.PENAUT_TIME),
            DriedFruit("almond", self.ALMOND_AMOUNT, self.ALMOND_TIME),
            DriedFruit("walnut", self.WALNUT_AMOUNT, self.WALNUT_TIME),
        ]
        self.selected_option = 0
        self.servo = Servo(
            pin_number=self.SERVO_PIN_NUMBER
        )
        self.lcd = LcdI2c(
            sda_pin_numb=self.LCD_SDA_PIN_NUMBER,
            scl_pin_numb=self.LCD_SCL_PIN_NUMBER
        )
        self.load_cell = LoadCell(
            dt_pin_numb=self.LOAD_CELL_DT_PIN_NUMBER,
            sck_pin_numb=self.LOAD_CELL_SCK_PIN_NUMBER
        )
        self.red_led = Led(
            pin_number=self.RED_LED_PIN_NUMBER
        )
        self.green_led = Led(
            pin_number=self.GREEN_LED_PIN_NUMBER
        )
        self.infra_red_cup = InfraRed(
            pin_number=self.INFRA_RED_CUP_PIN_NUMBER
        )
        self.infra_red_load = InfraRed(
            pin_number=self.INFRA_RED_LOAD_PIN_NUMBER,
            leds={"red": self.red_led, "green": self.green_led}
        )
        self.button_option = Button(
            pin_number=self.BUTTON_OPTION_PIN_NUMBER,
            handler_function=self.change_option
        )
        self.button_action = Button(
            pin_number=self.BUTTON_ACTION_PIN_NUMBER,
            handler_function=self.give_dried_fruit,
            infra_red= self.infra_red_cup
        )

        self.lcd.new_print(f"{self.get_dried_fruit().name}")
        self.servo.move(0)
        
    def get_dried_fruit(self):
        return self.dried_fruits[self.selected_option]
    
    def change_option(self):
        self.selected_option = (self.selected_option + 1) % len(self.dried_fruits)
        selected = self.get_dried_fruit()
        self.lcd.new_print(f"{selected.name}")
        print(f"Selected: {selected.name}")

    def open_gate(self):
        self.servo.move(90)

    def close_gate(self):
        self.servo.move(0)

    def give_dried_fruit(self):
        self.open_gate()
        sleep(self.get_dried_fruit().time)
        self.close_gate()

    def check20percentage(self):
        if self.infra_red_load.detect(): # mayor a 20
            self.green_led.turn_on()
            self.red_led.turn_off()
        else: # menor a 20
            self.green_led.turn_off()
            self.red_led.turn_off()