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

def validador_cadena(cadena, arbol, tipo, texto = ' Error. Vuelva a introducirlo: '):
    if tipo == 1:
        listacadenas = []
        for i in range(len(arbol)):
                lista = arbol[i]["genres"]
                for genero in lista:
                    listacadenas.append(genero)
        listacadenas = set(listacadenas)
    
    if tipo == 2:
        listacadenas = []
        for i in range(len(arbol)):
                lista = arbol[i]["actors"]
                for actor in lista:
                    listacadenas.append(actor)
        
        listacadenas = set(listacadenas)
    
    for i in listacadenas:
        if cadena.upper().replace('Á','A').replace('É','E').replace('Í','I').replace('Ó','O').replace('Ú','U') == i.upper().replace('Á','A').replace('É','E').replace('Í','I').replace('Ó','O').replace('Ú','U'):
            return i
    cadena = input(texto)
    return validador_cadena(cadena, arbol, tipo, texto)

def cantidad_peliculas_genero(genero,anyo,arbol):
    cantidad = 0
    for i in range(len(arbol)):
        if genero in arbol[i]["genres"] and anyo in arbol[i]["year"]:
            cantidad += 1
    return cantidad

with open("movies.json") as fichero:
    arbol = json.load(fichero)

print(cantidad_peliculas_genero(validador_cadena('drama',arbol,1),'2000', arbol))