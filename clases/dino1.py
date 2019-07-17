class Dino:
    ojos = 2
    def __init__(self, un_nombre, un_color, cantidad_patas=4, un_genero=None):
        self.nombre = un_nombre
        self.color = un_color
        self.patas = cantidad_patas
        self.genero = un_genero
        print("naci")

    def saludar(self):
        print("hola me llamo", self.nombre, "tengo", self.patas, "patas y soy", self.genero)

    def cortar_pata(self, cantidad_patas_a_cortar=1):
        self.patas = self.patas - cantidad_patas_a_cortar

    def decir_genero(self):
        print("hola soy", self.nombre, "y me identifico como", self.genero)

pepe = Dino("pepito", "verde",4,"macho alfa pecho peludo")
print(pepe.nombre)
pepe.saludar()

class perro:


    def __init__(self, un_nombre, una_raza, patas=4):
        self.nombre = un_nombre
        self.raza = una_raza
        self.patas = patas
        print("gauuu")

    def ladrar(self):
        print("pupi", self.nombre, "peluche", self.raza, ("y tiene" self.patas)



        print("pupi", self.nombre, "peluche", self.raza, ("y tiene" self.patas)
