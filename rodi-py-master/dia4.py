import rodi
import time

robot = rodi.RoDI()

# robot.move_forward()
# time.sleep(2)
# robot.move_right()
# time.sleep(0.5)
# robot.move_stop()
# robot.move_forward()
# time.sleep(2)
# robot.move_stop()
# robot.move_right()
# time.sleep(0.5)
# robot.move_stop()
# robot.move_forward()
# time.sleep(2)
# robot.move_right
# time.sleep(0.5)
# robot.move_stop()
# robot.move_forward()
# time.sleep(2)
# robot.move_stop()

# # forma for#

# for movimiento in range(4):
#     robot.move_forward()
#     time.sleep(2)
#     robot.move_left()
#     time.sleep(0.5)
#     robot.move_stop()

# # forma while#

# contador = 0
# while contador <= 3:
#     contador = contador + 1
#     robot.move_forward()
#     time.sleep(2)
#     robot.move_stop()
#     robot.move_left()
#     time.sleep(0.5)
#     robot.move_stop()

### -------------------- ###
# sensor a distancia

# print(robot.see(), "centimetro")

# variable = 3

# while True:
#     print(robot.see(), "centimetro")
#     robot.move_forward()

# try:
#     while True:
#         print(robot.see(), "centimetro")
#         robot.move_forward()
# except KeyboardInterrupt:
#     print("finalizado")
# #     robot.move_stop()

# try:
#     while True:
#         print(robot.see(), "centimetro")
#         if robot.see() <10:
#             robot.move_stop()
#             robot.move_backward()
#             time.sleep(1)
#             robot.move_right()
#             time.sleep(0.5)
#         else :
#             robot.move_forward()

# except KeyboardInterrupt:
#     print("finalizado")
#     robot.move_stop()



# try:
#     while True:
#         print(robot.see(), "centimetro")
#         if robot.see()>15:
#             robot.move_stop()
#             robot.move_right()
        
#         else:
#             robot.move_forward()

# except KeyboardInterrupt:
#     print("finalizado")
#     robot.move_stop()


# try:
#     x = 0
#     while True:
#         cm = robot.see()
#         if cm<=15:
#             robot.move_forward()
#         else:
#             robot.move_stop()
#             robot.move_right
#             time.sleep(0.5)
#         robot.pixel(x,x,x)
#         time.sleep(0.1)
#         X=X+1
# except KeyboardInterrupt:
#     print("finalizo")
#     robot.move_stop()

while True:
    print(robot.light())
    time.sleep(0.5)
    robot.sing(5800,1000)

while True:
    linea = robot.sense()
    print(linea)
    print(linea[0])
    print(linea[1])
    print(linea[0.5])