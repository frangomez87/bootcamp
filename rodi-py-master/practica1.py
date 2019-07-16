import RPi.GPIO as gpio
from time import sleep
led = 23
gpio.setmode(gpio.BCM)

gpio.setmode(led1.gpio.OUT)

while True:
    gpio.output(led1, True)
    sleep(1)
    gpio.output(led1, False)
    sleep(1)

# ejercicio
# hacer que los tres lees parpaden todos juntos con un intervalo
#  de 0.5 segundos
# pista: led2 = 24
#        led3 = 25