import json
from funciones import menu

with open( "movies.json" ) as fichero :
    arbol = json.load( fichero )

menu( arbol )