import json

def duracion_formato(duracion):
    duracion = int(duracion.replace('PT','').replace('M',''))
    hora = int(duracion/60)
    min = duracion - hora*60
    if min == 0:
        if hora == 1:
            return str(hora) + " hora"
        return str(hora) + " horas"
    return str(hora) + " horas y " + str(min) + " minutos"

def listar_peliculas(arbol):
    lista = []
    for i in range(len(arbol)):
        lista.append((arbol[i]["title"],arbol[i]["year"], duracion_formato(arbol[i]["duration"])))

    return lista

def cantidad_peliculas_genero(genero,anyo,arbol):
    cantidad = 0
    for i in range(len(arbol))
        if genero in arbol[i]["genres"] and anyo in arbol[i]["year"]:
            cantidad += 1
    return cantidad

with open("movies.json") as fichero:
    arbol = json.load(fichero)
