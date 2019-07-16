print(2+2)
print(2*10)
print(4*5)
print(6+5)
print("hola mundo")
print("buen dia")
print("2+2")
print("hola "*100)
a = 2*2
b = 10+3
c = -17
print(a+b+c)
print("hola", 2, "chau", 10,)
nombre = "francisco"
edad = 31
hobby = "pintar"
print("hola, me llamo", nombre, "y tengo", edad, "y mi hobby es", hobby)
lista_vacia = []
listax = [1,2,6,8]
print(lista_vacia)
print(listax)
datos = ["francisco"]
print(datos)
datos = ["francisco", 31]
print("hola mi nombre es", datos[0],"y tengo", datos[1])
datos[1] = 40
print("hola mi nombre es", datos[0], "y tengo", datos[1])
datos.append("serigrafista")
print(datos)
print(datos[2])
datos.append("disenar")
datos.append("pintar")
print(datos)
datos.pop()
print(datos)
datos.pop()
print(datos)
print(len(datos))
saludo = "hola, que tal"
print(saludo)
print(len(saludo))
saludo = "buenos dias, buenas tardes"
print(saludo)
print(len(saludo))
print("la lista de datos tiene", len(datos), "elemento")
print(datos)
ultimo=len(datos)-1
print("el ultimo valor es", datos[ultimo])
lista_temas = ["variables","listas", "tipos de temas"]
for concepto in lista_temas:
    print("hoy aprendi"), concepto
    print("que gusto")
    print("esto lo que aprendi")
lista_temas = ("disenar", "pintar",)
for concepto in lista_temas:
    print(concepto, "??")
    print("q bueno")
for x in range (10):
    print(x)