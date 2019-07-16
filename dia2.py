#imprimir el ultimo elemento de una lista sin saber cuandos
#elemento tiene, solucion general
otra_lista = [5,"hola que tal","chau",4]
otra_lista.append("aaaa")
#solucion paso a paso
din_lista = len(otra_lista)
print("la dimension de otra_lista es", din_lista)
indice_de_ultimo = din_lista -1
print(otra_lista[indice_de_ultimo])
#solucion de una lista
print(otra_lista[len(otra_lista)-1])
#esto es equivalente
for numero in range(1,11):
    print(numero)
#imprimir hola 10 veces
for numero in [1,2,3,4,5,6,7,8,9,10]:
    print("hola", numero)#imprimir numero opcionai
#imprimir el numero de resultado de la suma de los numeros
#del 1 al 10  55
challenge = [1,2,3,4,5,6,7,8,9,10] # se crea una lista
a=0                         #se crea una variable de base
for x in challenge:
    a=a+x
print(a)
sumatoria=0
for valor in range(1,11):
    sumatoria = sumatoria + valor
print(sumatoria)
####### FUNCIONES###### 
def suma  (nume1, num2):
    resultado = nume1+num2
    return resultado
#equivalente a la de arriba
def suma2(num1, num2):
    return num1 + num2
print(suma(5,10))
resul = suma(5,8)
print(resul)
#crear una funcion resta,que reciba como parametrode dos numeros
#y retorne la resta de esos numeros
#crear una funcion saludo2 que reciba como parametro nombre y edad
# e imprima "hola soy ___ y tengo___ anos"
#llamar varias veces a la funcion con distintos valores
#nota:retornar es algo apcional
def colorear(pintar,borrar):
    revelar = pintar + borrar
    return revelar
print(colorear(5,5))

def colorear2(pintar,borrar):
    revelar = pintar - borrar
    return revelar
print(colorear(5,5))
print(colorear2(7,7))

def saludo(nombre, edad):
    print("hola soy", nombre, "y tengo", edad, "anos")
saludo("francisco", 31)

#ej. crear una funcion suma_lista que reciba como argumento una lista de numero
#y retorne la suma de sus elemento
#pista: usan acomulador

lista = [1,2,3,4,5]
def lista_suma(numero):
    suma=0
    for x in numero:
        suma=suma + x
    return suma
print(lista_suma(lista))

lista2 = [1,2,3,4,5,6,7,8,9,10]
def lista_suma2(numero2):
    suma=0
    for x in numero2:
        suma=suma + x
    return suma
print(lista_suma2(lista2))

def lista_cuadrado(listajeyma):
    a = []
    for jeyma in listajeyma:
        a.append(jeyma * jeyma)
    return a
otraves = [1,4,9,16,25]
resultado_cuad = lista_cuadrado(otraves)
print(resultado_cuad)

# eliminar todos los elementosde una lista utilizando "for"

grupo5 = ["n","f1","f2","a"]
print("antes", grupo5)
for j in range(len(grupo5)):
    grupo5.pop()
print("despues", grupo5)

# crear una funcion suma_cuadrado que reciba una de lista de numeros
# y retorne el valor de la suma de cada numero al cuadrado
# [1,2,3,4] --- 1+4+9+16 --- 30

lista_numeros = [1,2,3,4,]
def suma_cuadrado(lista_n):
    suma = 0
    for p in lista_n:
        suma = suma + (p*p)
    return suma
print(suma_cuadrado(lista_numeros))
def suma_cuadrado2(lista_n):
    return suma_cuadrado2(lista_cuadrado(lista_numeros))
print(suma_cuadrado2(lista_numeros))