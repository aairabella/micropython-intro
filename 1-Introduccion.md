# Introducción

Este tutorial está desarrollado para ser ejecutado en una computadora con GNU/Linux.

## Verificar UART

En una terminal, se puede abrir `dmesg` para ver si detecta bien el converosr USB a Serie.

`sudo dmesg -w`

Se conecta la placa utilizando un cable USB-MicroUSB. 

La ventana de la terminal con `dmesg` debe mostrar algo como:

```
[20273.803488] usb 1-4: new full-speed USB device number 40 using xhci_hcd
[20273.945198] usb 1-4: New USB device found, idVendor=10c4, idProduct=ea60
[20273.945204] usb 1-4: New USB device strings: Mfr=1, Product=2, SerialNumber=3
[20273.945208] usb 1-4: Product: CP2104 USB to UART Bridge Controller
[20273.945211] usb 1-4: Manufacturer: Silicon Labs
[20273.945215] usb 1-4: SerialNumber: 011E666D
[20273.946487] cp210x 1-4:1.0: cp210x converter detected
[20273.947163] usb 1-4: cp210x converter now attached to ttyUSB0
```
Luego, se verifica que nombre le asignó al dispositivo ejecutando:

`ls -la /dev /ttyUSB*`

Cuya salida dará algo como: 

`crw-rw---- 1 root dialout 188, 0 mar 24 16:07 /dev/ttyUSB0`

Se observa que le asigno el nombre `ttyUSB0`. A partir de este momento, se deberá utilizar este dispositivo como nombre para todos los casos en que se requiera conectar a la placa desde la PC.

## Instalación de paquetes necesarios

Abra una terminal y ejecute:

`pip install esptool`

## Borrar el contenido de la memoria en el ESP32
Luego, es necesario borrar el contenido de la memoria. En la misma terminal ejecute:

`esptool.py --port /dev/ttyUSB0 erase_flash`

Debería aparecer un mensaje similar al siguiente:
```
esptool.py v2.7
Serial port /dev/ttyUSB0
Connecting.......
Detecting chip type... ESP32
Chip is ESP32D0WDQ6 (revision 0)
Features: WiFi, BT, Dual Core, Coding Scheme None
Crystal is 40MHz
MAC: 24:0a:c4:01:a6:58
Uploading stub...
Running stub...
Stub running...
Erasing flash (this may take a while)...
```

## Descargar Firmware e instalarlo en la placa

Descargar de [este link](https://micropython.org/download#esp32) el firmware que corresponda a su placa.

Por ejemplo, como se muestra en la siguiente imagen, para este tutorial se descargó la versión

`esp32-idf3-20200324-v1.12-270-g38ccb4c64.bin `

![](/home/andres/micropython-intro/pics/download_version.png) 

Para cargar este firmware a la placa se debe ejecutar:

`esptool.py --chip esp32 --port /dev/ttyUSB0 --baud 460800 write_flash -z 0x1000 esp32-idf3-20200324-v1.12-270-g38ccb4c64.bin`

Para verificar si el firmware se instaló correctamente se puede ejecutar una consola UART y ver como bootea el mismo. Con la placa conectada, ejecutar:

`sudo minicom -D /dev/ttyUSB0 -b 115200`

Luego presionar el boton de reset de la placa. En la consola se debería ver algo similar a:

```
ets Jun  8 2016 00:22:57

rst:0x1 (POWERON_RESET),boot:0x13 (SPI_FAST_FLASH_BOOT)
ets Jun  8 2016 00:22:57

rst:0x10 (RTCWDT_RTC_RESET),boot:0x13 (SPI_FAST_FLASH_BOOT)
configsip: 0, SPIWP:0xee
clk_drv:0x00,q_drv:0x00,d_drv:0x00,cs0_drv:0x00,hd_drv:0x00,wp_drv:0x00
mode:DIO, clock div:2
load:0x3fff0018,len:4
load:0x3fff001c,len:5008
ho 0 tail 12 room 4
load:0x40078000,len:10600
ho 0 tail 12 room 4
load:0x40080400,len:5684
entry 0x400806bc
I (541) cpu_start: Pro cpu up.
I (541) cpu_start: Application information:
I (541) cpu_start: Compile time:     Mar 24 2020 12:39:05
I (545) cpu_start: ELF file SHA256:  0000000000000000...
I (551) cpu_start: ESP-IDF:          v3.3.1
I (555) cpu_start: Starting app cpu, entry point is 0x400836ec
I (0) cpu_start: App cpu up.
I (566) heap_init: Initializing. RAM available for dynamic allocation:
I (573) heap_init: At 3FFAFF10 len 000000F0 (0 KiB): DRAM
I (579) heap_init: At 3FFB6388 len 00001C78 (7 KiB): DRAM
I (585) heap_init: At 3FFB9A20 len 00004108 (16 KiB): DRAM
I (591) heap_init: At 3FFBDB5C len 00000004 (0 KiB): DRAM
I (597) heap_init: At 3FFCC810 len 000137F0 (77 KiB): DRAM
I (603) heap_init: At 3FFE0440 len 00003AE0 (14 KiB): D/IRAM
I (610) heap_init: At 3FFE4350 len 0001BCB0 (111 KiB): D/IRAM
I (616) heap_init: At 40099A80 len 00006580 (25 KiB): IRAM
I (622) cpu_start: Pro cpu start user code
I (305) cpu_start: Starting scheduler on PRO CPU.
I (0) cpu_start: Starting scheduler on APP CPU.
MicroPython v1.12-270-g38ccb4c64 on 2020-03-24; ESP32 module with ESP32
Type "help()" for more information.
```

En la ante última línea indica la versión de MicroPython instalada, la cual se corresponde a la descargada en el primer paso.