from machine import Pin, Timer
from time import sleep
from util.program import Program

# Configuramos el pin del botón y la función de interrupción
# button = Pin(19, Pin.IN, Pin.PULL_UP)

# Creamos un temporizador
# timer = Timer(0)
# count = 0
# # Definimos la función que se llamará cuando el temporizador expire
# def debounce(timer):
#     # Si el botón sigue siendo presionado después de 50ms, realizamos la acción
#     if button.value() == 0:
#         global count
#         count += 1
#         print(f"Hola mundo {count}")

# # Definimos la función de interrupción del botón
# def button_pressed(pin):
#     # Detenemos el temporizador (si está en ejecución) y lo reiniciamos
#     timer.deinit()
#     timer.init(mode=Timer.ONE_SHOT, period=50, callback=debounce)

# # Asignamos la función de interrupción al pin del botón
# button.irq(trigger=Pin.IRQ_FALLING | Pin.IRQ_RISING, handler=button_pressed)


def main():
    program = Program()
    program.run()

if __name__ == '__main__':
    main()