from components.button import Button
from components.infraRed import InfraRed
from components.lcdI2c import LcdI2c
from components.servo import Servo
from components.loadCell import LoadCell
from components.led import Led
from time import sleep
from math import floor


class DriedFruit:
    def __init__(self, name, amount, time, opening):
        self.name = name
        self.amount = amount
        self.time = time
        self.opening = opening


class Dispenser:
    PENAUT_AMOUNT = 50
    ALMOND_AMOUNT = 100
    WALNUT_AMOUNT = 80

    PENAUT_TIME = 0.7
    ALMOND_TIME = 0.7
    WALNUT_TIME = 0.7

    PENAUT_OPENING = 50
    ALMOND_OPENING = 80
    WALNUT_OPENING = 80

    CLOSE_GATE = 0

    SERVO_PIN_NUMBER = 14
    LCD_SDA_PIN_NUMBER = 4
    LCD_SCL_PIN_NUMBER = 5
    LOAD_CELL_DT_PIN_NUMBER = 33
    LOAD_CELL_SCK_PIN_NUMBER = 32
    INFRA_RED_CUP_PIN_NUMBER = 23
    INFRA_RED_LOAD_PIN_NUMBER = 25
    LED_RED_PIN_NUMBER = 26
    LED_GREEN_PIN_NUMBER = 15
    BUTTON_OPTION_PIN_NUMBER = 19 # AZUL
    BUTTON_ACTION_PIN_NUMBER = 2 # VERDE

    def __init__(self):
        self.dried_fruits = [
            DriedFruit("mani", self.PENAUT_AMOUNT, self.PENAUT_TIME, self.PENAUT_OPENING),
            DriedFruit("almendra", self.ALMOND_AMOUNT, self.ALMOND_TIME , self.ALMOND_OPENING),
            DriedFruit("nuez", self.WALNUT_AMOUNT, self.WALNUT_TIME , self.WALNUT_OPENING),
        ]
        self.selected_option = 0
        self.selected_fruit = self.get_dried_fruit()
        self.selected_fruit_text = f"{self.selected_fruit.name} {self.selected_fruit.amount} g"
        self.last_weight = 0
        self.servo = Servo(
            pin_number=self.SERVO_PIN_NUMBER
        )
        self.lcd = LcdI2c(
            sda_pin_numb=self.LCD_SDA_PIN_NUMBER,
            scl_pin_numb=self.LCD_SCL_PIN_NUMBER
        )
        self.load_cell = LoadCell(
            dt_pin_numb=self.LOAD_CELL_DT_PIN_NUMBER,
            sck_pin_numb=self.LOAD_CELL_SCK_PIN_NUMBER,
            calibration_factors=[2311, -49688]
        )
        self.led_red = Led(
            pin_number=self.LED_RED_PIN_NUMBER
        )
        self.led_green = Led(
            pin_number=self.LED_GREEN_PIN_NUMBER
        )
        self.infra_red_cup = InfraRed(
            pin_number=self.INFRA_RED_CUP_PIN_NUMBER
        )
        self.infra_red_load = InfraRed(
            pin_number=self.INFRA_RED_LOAD_PIN_NUMBER,
        )
        self.button_option = Button(
            pin_number=self.BUTTON_OPTION_PIN_NUMBER,

        )
        self.button_action = Button(
            pin_number=self.BUTTON_ACTION_PIN_NUMBER,
        )

        self.initialize_components()

    def get_dried_fruit(self):
        self.selected_fruit = self.dried_fruits[self.selected_option]
        self.selected_fruit_text = f"{self.selected_fruit.name} {self.selected_fruit.amount}g"
        return self.selected_fruit

    def change_option(self):
        print("llamando a change_option")
        self.selected_option = (self.selected_option +
                                1) % len(self.dried_fruits)
        self.get_dried_fruit()
        self.lcd.new_print(self.selected_fruit_text)

    def open_gate(self):
        self.servo.move(self.selected_fruit.opening)

    def close_gate(self):
        self.servo.move(self.CLOSE_GATE)

    def give_dried_fruit(self):
        print("llamando a give_dried_fruitn")
        self.get_dried_fruit()
        if self.infra_red_cup.detect():
            self.load_cell.get_value()
            self.last_weight = self.load_cell.get_value()
            current_weight = self.load_cell.get_value() - self.last_weight
            
            while current_weight <= self.get_dried_fruit().amount:
                self.lcd.new_print(f"Peso actual:\n{current_weight:0.3f} g")
                self.open_gate()
                sleep(self.get_dried_fruit().time)
                self.close_gate()
                self.load_cell.get_value()
                current_weight = floor(
                    self.load_cell.get_value() - self.last_weight)
                print(f"Peso actual: {current_weight}")

            self.close_gate()
            self.last_weight = self.load_cell.get_value()
            self.lcd.clear()
            self.lcd.print(f"Vaso rellenado\n{current_weight:0.3f} g", 2, True)
            self.lcd.new_print(self.selected_fruit_text)

        else:
            self.lcd.clear()
            self.lcd.print("Falta vaso", 2, True)
            self.lcd.new_print(self.selected_fruit_text)

    def check20percentage(self):
        print(self.infra_red_load.detect())
        if self.infra_red_load.detect():  # mayor a 20
            self.led_green.turn_on()
            self.led_red.turn_off()
        else:  # menor a 20
            self.led_green.turn_off()
            self.led_red.turn_on()

    def initialize_components(self):
        self.button_option.add_event(handler_function=self.change_option)
        self.button_action.add_event(handler_function=self.give_dried_fruit)

        self.infra_red_load.add_event(handler_function=self.check20percentage)

        self.lcd.new_print(self.selected_fruit_text)
        self.servo.move(0)
