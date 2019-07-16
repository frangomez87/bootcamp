import rodi
import time


robot = rodi.RoDI()                     #instanciamos un objeto RoDI

while True:
    linea = robot.light()               #leemos e imprimimos la lectura del sensor de luz
    time.sleep(0.5)
    print(linea)


