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

def lista_cadenas(apartado, arbol):
    listacadenas = []
    for i in range(len(arbol)):
            lista = arbol[i][apartado]
            for unidad in lista:
                listacadenas.append(unidad)
    listacadenas = set(listacadenas)
    print(listacadenas)
    return listacadenas

def validador_cadena(cadena, arbol, apartado, texto = ' Error. Vuelva a introducirlo: '):
    for i in lista_cadenas(apartado,arbol):
        if cadena.upper().replace('Á','A').replace('É','E').replace('Í','I').replace('Ó','O').replace('Ú','U') == i.upper().replace('Á','A').replace('É','E').replace('Í','I').replace('Ó','O').replace('Ú','U'):
            return i
    cadena = input(texto)
    return validador_cadena(cadena, arbol, tipo, texto)

def cantidad_peliculas_genero(genero,anyo,arbol):
    genero = validador_cadena(genero,arbol,'genres')    
    cantidad = 0
    for i in range(len(arbol)):
        print (i)
        if genero in arbol[i]["genres"] and anyo > arbol[i]["year"]:
            cantidad += 1
    return cantidad

with open("movies.json") as fichero:
    arbol = json.load(fichero)

print(cantidad_peliculas_genero('Drama','1600', arbol))