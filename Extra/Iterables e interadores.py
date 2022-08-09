#Iterables: Objetos que podemos recorrer usando un ciclo. Ej:
## Cadenas de texto
## Listas
## Tuplas
## Diccionarios

# itaradores: Objetos  que permiten recorrer objetos iterables
## iter(): Recibe el objeto iterable, crea un iterador y permite recorrer los elementos que lo componen
## next(): Recibe el iterador creado y cada vez que se la invoca retorna el elemento siguiente

lista = [1, 2, 3]
iterador = iter(lista)
print(next(iterador))
print(next(iterador))
print(next(iterador))