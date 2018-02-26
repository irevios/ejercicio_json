# Ejercicio JSON
[LM] - Proyecto 2ª evaluación

## Enunciado
El archivo [movies.json](movies.json) contiene información de las películas mejor valoradas. Se crearán los ejercicios correspondientes a la siguiente lista:

* Listar el título, año y duración de todas las películas.
* ¿Cuántas películas tienen el género drama y son posteriores a un año dado?
* Mostrar las películas que contengan en la sinopsis dos palabras dadas.
* Mostrar las películas en las que ha trabajado un actor dado.
* Mostrar el título y la url del póster de las tres películas con una media de puntuaciones más alta y lanzadas entre dos fechas dadas.

## Árbol del JSON

```
películas
 ├── película [01]
 │	 ├── titulo
 │	 ├── año
 │	 ├── género
 │	 │	 ├── género [01]
 │	 │	 └── género [02]
 │	 ├── puntuaciones
 │	 │	 ├── puntuación [01]
 │	 │	 ├── puntuación [02]
 │	 │	 │	.
 │	 │	 │	.
 │	 │	 └── puntuación [30]
 │	 ├── duración
 │	 ├── fecha lanzamiento
 │	 ├── titulo original
 │	 ├── sinopsis
 │	 ├── actores
 │	 │	 ├── actor [01]
 │	 │	 ├── actor [02]
 │	 │	 └── actor [03]
 │	 └── url póster
 │
 ├── película [02]
 │	.
 │	.
```
