import requests

KEY = "4e9fcd9d"
URL = "http://www.omdbapi.com/?apikey="
titulo = "the matrix"

busqueda = URL + KEY + "&t=" + titulo
resultado = requests.get(busqueda)
diccionario_peli = resultado.json()
print(diccionario_peli)

# crear una funcion que reciba como parametro el nombre de una 
# pelicula y que retorne el nombre del director de la pelicula
# usando API de OMDB
print(diccionario_peli["Director"])

def pelisxx(diccionario_peli):
    busqueda = URL + KEY + "&t=" + titulo
    resultado = requests.get(busqueda)
    return resultado.jpson()["Director"]

print(pelisxx("the matrix"))