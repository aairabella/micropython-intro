# Cargar programa

Conectarse a la placa usando `rshell`:

`rshell -p /dev/ttyUSB0 -b 115200 --quiet`

Copiar el programa que se desea ejecutar:

`cp ejemplos/1-blinky/main.py /pyboard/`

Salir del `rshell`:

`exit`

Reiniciar la placa