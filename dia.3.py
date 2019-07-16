ing_pan = ["harina", "levadura", "sal", "azucar", "agua"]

def imprimir_lista(ingredientes, nombre_producto):
    print("lista de compras de", nombre_producto)
    print("___________________")
    for producto in ingredientes:
        print(producto)

imprimir_lista(ing_pan, "pan")

ing_salsa = ["tomate","azucar", "sal", "cebolla"]
imprimir_lista(ing_salsa, "salsa de pizza")

######### condiciones#######

# == igual
# > mayor que
# < menor que
# >= mayor o igual que
# <= menor o igual que
# != distinto o no igual

a = 3
# pregunta 1
if a > 3:
    print("si, a es mayor que 3")
    print("chau!")
else:
    print("no, a no es mayor a 3")
# pregunta 2
if a == 3:
    print(" es igual a 3")

nota = 60
#pregunta 3
if nota >= 60:
    print("pasasteeeeee")
else:
    print("hule ya")
# ej. crear una funcion que reciba como parametro una
# nota de 1 a 100 e imprimir si pasaste o te aplazaste

def resultado(nota, nombre):
    if nota > 50:
        print("lo logreeee pase", nombre)
    else:
        print("aplazado",nombre)
resultado(55,"francisco")

a = 6
if a > 5 and a < 10:
    print("a es mayor a 5  y menor que 10")
else:
    print("a no esta en el rango, algunas de la 2 condiciones no se cumplieron")

if a > 5 or a < 10:
    print("a es mayor que 5 o menor que 10")
else:
    print("a no es mayor que 5 ni menor que 10")

edad = 7
if edad > 18:
    print("deeria estar en la universidad")
elif edad > 13:
    print("deeria estar en secundaria")
elif edad > 6:
    print("deberia estar en primaria")
else:
    print("deberia estar en su casa bbdlc")
#anidado
if edad > 18:
    print("universidad")
else:
    if edad > 13:
        print("secundaria")
    else:
        if edad > 6:
            print("primaria")
        else:
            print("bbdlc")

# ej. crear una funcion puntaje que reciba como parametro una nota
# del 1 al 100 e imprimir que nota sacaste
# nota < 60 -----> 1
# nota entre 60 y 70 ---> 2
# nota entre 71 y 75 ---> 3
# nota entre 76 y 85 ---> 4
# nota mayor que 85 ----> 5


def calificacion(punto_final, nombre):
    if punto_final < 60:
        print("tu nota es 1", nombre)
    elif punto_final > 60 and punto_final < 70:
        print("tu nota es 2", nombre)
    elif punto_final > 71 and punto_final < 75:
        print("tu nota es 3", nombre)
    elif punto_final > 76 and punto_final < 85:
        print("tu nota es 4", nombre)
    elif punto_final > 85 and punto_final <101:
        print("tu nota es 5", nombre)
calificacion(80, "judit")
calificacion(55, "ruben")
calificacion(79, "francisco")
calificacion(67, "jenny")
calificacion(90, "arnaldo")

# ej. pedir al usuario que ingrese de 3 numerosy multiplicarlos
# entre  si, imprimir resultado
int("22") + 3 # ---> 25
 
# ej2. pedir al usuario un numero del 1 a 100 y llamar a la
# funcion que retornaba la nota que creamos hace un rato
# utiizando el valor ingresando por el usuario

francisco = input("ingresa tu nombre")
print(francisco)
francisco1 = input("primero :")
francisco2 = input("segundo :")
francisco3 = input("tercero :")
sumar = int(francisco1) * int(francisco2) * int(francisco3)
print(sumar)

#### bucle while == mientras ####

x = 74956
while x != 5:# mientras x sea distinto de 5 hacer lo siguiente
    print("hola esto es un bucle while, se ejecutar mientras  x sea distinto")
    x = int(input("ingresa un numero"))#ingresamso un valor x
    print("el valor de x ahora es", x)
print("termino!!!")

# contador inverso
contador = 10
while contador > 0:
    print("sigo enele bucble while")
    contador = contador -1
    print("te quedan", contador, "oportunidades")
print("termino")
#contador
contador = 0
while contador < 10:
    print("sigo en el bucle while")
    contador = contador +1
    print("se repitio", contador, "veces")

# usando while pedir al usuario 5 ingredientes para hacer una pizza
# y agregar a una lista, al final imprimir la lista

pizza = 0
pedidos = []
while pizza < 5:
    print("muzzarella:")
    lista_pedido = input("cocinero..:")
    pedidos.append(lista_pedido)
    pizza = pizza +1
print("el pedido es:", pedidos)


adivino = False

while adivino == False:
    apuesta = input("adivina el numero secreto de 1 al 10: ")

    if int(apuesta) == numero_secreto
        print("GANASTEEE..!")
        adivino = True
    else:
        print("segui participando nde arruinado")

# ej. crear un juego de adivinar el numero como el de arriba y
# darle pistas al usuario si el numero que ingreso es mayor o menor
# al adivinar
# pista usar elif

# ej. buscar como generar un numero aleatorio para numero_secreto

advinar = False
numero_secreto = 20
while adivinar == False:
    apuesta = input(" advinar en numer_secreto de 1 al 30")
    if int(apuesta) == numero_secreto:
        print("ganasteeeee..!!")
        varios = True
    elif numero_secreto > int (apuesta):
        print("el numero es mayor")
    elif numero_secreto < int (apuesta):
        print