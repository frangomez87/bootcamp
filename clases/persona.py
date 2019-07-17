# class Persona: # defienimos la clase, una receta para craer un objeto
#     edad = 0   # o tambien la clase es la plantilla
#     nacionalidad = "paraguaya"               # atribito de clase o propiedad del objeto q vamos a crear

#     def __init__(self, un_nombre): #___init__ es el metodo de constructor
#                                    # metodos -->funciones dentro de una clase
#         self.mi_nombre = un_nombre # usamos self para referirnos al objeto mismo
#         print("hola naci, me llamo", self. mi_nombre) 

#     def cumple(self): # cumple es un metodo de la clase persona
#         self.edad = self.edad +1# que aumenta la propiedad en 1

#     def asignar_edad(self, una_edad):# asignar es un metodo que recibe un
#         self.edad = una_edad         # argumento numero y asignar a la propiedad
#         print("hola soy", self.)                   # edad del objeto
                                     
# pepe = Persona("pepito")            # pepe es objeto de la clase persona
# pepa = Persona("pepita")
# nacio = Persona("fran")
# print(pepe.edad)
# print(pepe.mi_nombre)
# pepe.cumple()
# print(pepe.edad)
# print(nacio.nacionalidad)

# ej. agragar un metodo a la clase persona que asigne una nacionalidad y otro
# metodo saludar que imprima "hola soy ___ y mi nacionalidad es___"



# hacer una clase que se llame vehiculo y que tenga tres atributos y uno de
# que sea cantidad_rueda, y un metodo que sea definir_tipo_vehiculo que me
#diga si es "bicicleta, triciclo, auto" de acuerdo a la cantidad de rueda.


class vehiculo:
    rueda = 0
    color = ""
    marca = ""
    def __init__(self, cantidad_rueda):
        self.rueda = cantidad_rueda 

    def definir_tipo_vehiculo(self):
        if self.rueda == 2:
            print("auto")

toyota = vehiculo(2)
toyota.definir_tipo_vehiculo()
