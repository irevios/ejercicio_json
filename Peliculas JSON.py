import json
import os

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
            if type(lista) == list:
                for unidad in lista:
                    listacadenas.append(unidad)
            else:
                listacadenas = lista
    listacadenas = set(listacadenas)
    return listacadenas

def validador_cadena( cadena, arbol, apartado, texto = ' Error. Vuelva a introducirlo: '):
    for i in lista_cadenas(apartado,arbol):
        if cadena.upper().replace('-','').replace('Á','A').replace('É','E').replace('Í','I').replace('Ó','O').replace('Ú','U') == i.upper().replace('-','').replace('Á','A').replace('É','E').replace('Í','I').replace('Ó','O').replace('Ú','U'):
            return i
    cadena = input(texto)
    return validador_cadena(cadena, arbol, tipo, texto)

def cantidad_peliculas_genero( genero, anyo, arbol):
    genero = validador_cadena(genero,arbol,'genres')    
    cantidad = 0
    for i in range(len(arbol)):
        if genero in arbol[i]["genres"] and int(anyo) < int(arbol[i]["year"][0:4]):
            cantidad += 1
    return cantidad

def buscar_sipnosis( palabra1, palabra2, arbol ):
    lista = []
    for i in range(len(arbol)):
        sipnosis = arbol[i]["storyline"]
        if palabra1 in sipnosis and palabra2 in sipnosis:
            lista.append((arbol[i]["title"],sipnosis))
    
    return lista

def buscar_por_actor( actor, arbol ):
    lista=[]
    actor = validador_cadena(actor,arbol,'actors')
    for i in range(len(arbol)):
        if actor in arbol[i]['actors']:
            lista.append(arbol[i]['title'])
    return lista

def dias_del_mes ( mes, anyo ) :
    if anyo % 400 == 0 or anyo % 4 == 0 and anyo % 100 != 0:
        feb = 29
    
    else: 
        feb = 28

    dias = [ 31, feb, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ]
    return dias[ mes - 1 ]

def validador_fecha(fecha):
    if len(fecha.split('/')) == 3:
        fecha = fecha.split( "/" )
        dia,mes, anyo = int(fecha[0]),int(fecha[1]),int(fecha[2])
        if mes >= 1 and mes <= 12 and dia >= 1 and dia <= dias_del_mes( mes, anyo ):
            return str(anyo)+'-'+str(mes)+'-'+str(dia)
    fecha = input(' Debe tener el formato "DD/MM/AAAA".\n Vuelva a intentarlo: ')
    return validador_fecha(fecha)

def top_tres(fecha1,fecha2,arbol):
    lista=[]
    for i in range(len(arbol)):
        puntuacion = round(sum(arbol[i]['ratings'])/len(arbol[i]['ratings']),2)
        if validador_fecha(fecha1) <= arbol[i]['releaseDate'] and validador_fecha(fecha2) >= arbol[i]['releaseDate']:
            lista.append((arbol[i]['title'],arbol[i]['posterurl'],puntuacion,))
        
    lista = sorted(lista,key=lambda x: x[2], reverse=True)
    return lista[0:3]

def menu(arbol):
    opcion = 0
    while ( opcion != 6) :
        os.system( 'clear' )
        print( '\n PELÍCULAS EN ARCHIVO JSON\n {}\n 1 - Listar películas\n 2 - Cantidad de películas por género y posterior a año\n 3 - Buscar película por dos palabras en sipnosis\n 4 - Buscar película por actor\n 5 - Top 3 películas entre dos años\n 6 - Salir'.format( '=' * 23 ) )
        opcion = int( input( ' Opción: ' ) )
        if opcion == 1 :
            for i in listar_peliculas( arbol ) :
                print( ' Título: {}\n Año: {}\n Duración: {}\n'.format( i[0], i[1], i[2]) )
        if opcion == 2 :
            genero = validador_cadena( input( ' Género: ' ), arbol, "genres", ' Género Incorrecto (¡Debe estar en inglés!).\n Género: ' )
            anyo = input( ' Posterior al año: ' )
            print( ' Películas con el género "{}" y posteriores al año "{}": {}'.format( genero, anyo, cantidad_peliculas_genero(genero, anyo, arbol ) ) )
        
        if opcion == 3 :
            palabra1 = input( " Deben estar en inglés. \n Primera palabra: ")
            palabra2 = input(" Segunda palabra: ")
            for i in buscar_sipnosis(palabra1,palabra2,arbol) :
                print( ' Título: {}\n Sipnosis: {}\n'.format( i[0], i[1] ) )


with open("movies.json") as fichero:
    arbol = json.load(fichero)

menu(arbol)