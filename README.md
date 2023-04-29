# Máquina dispensadora de frutos secos

Este proyecto consiste en la creación de una máquina dispensadora de frutos secos, diseñada para facilitar el consumo de maní, almendras y nueces en porciones precisas.

## Características

- Dispensa porciones precisas de maní, almendras y nueces: maní 50g, almendra 100g y nueces 80g.
- Interfaz visual simple y cómoda para visualizar el contenido del fruto seco dispensado en ese momento.
- Dos botones para cambiar la carga de maní a almendras y luego a nueces, y el otro para dispensar la carga.
- Sensor infrarrojo para detectar la presencia de un vaso o recipiente antes de dispensar la carga.
- Indicador de estado con dos luces: verde si tiene más del 20% de producto y roja si tiene menos del 20%, para que el usuario siempre sepa cuánto producto queda en la máquina.

## Tecnologías utilizadas

- ESP32
- Sensor infrarrojo
- Luces LED
- Botones 
- Componentes electrónicos diversos

## Instalación

1. Clonar el repositorio en la ubicación deseada.
2. Conectar los componentes electrónicos según el esquema de circuito proporcionado.
3. Cargar el código fuente en el Arduino utilizando el software de programación adecuado.
4. Encender la máquina dispensadora y disfrutar de porciones precisas de maní, almendras y nueces.

## Esquema de pines del ESP32

Revisar archivo [dispenser.py](https://github.com/jorgeplazadelosreyes/P1_embebidos/blob/main/util/dispenser.py)

SERVO: pin 14

PANTALLA LCD:

- pin sda 4
- pin scl 5
CELDA DE CARGA:

- pin dt 33
- pin sck 32

INFRAROJO PARA VASO: pin 23

INFRAROJO PARA CARGA: pin 25

LED ROJO: pin 26

LED VERDE: pin 15

BOTON CAMBIO DE OPCION: pin 19

BOTON ACCIONADOR: pin 2
