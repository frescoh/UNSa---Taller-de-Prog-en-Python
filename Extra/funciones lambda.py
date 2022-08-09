# Creacion basica de una funcion lambda
lambda x: x**2

#Uso basico de una funcion lambda para mostrar resultado sin almacenarlo
print((lambda x: x**2)(2))

# Almacenamiento de una funcion lambda en una variable
cuadrado= lambda x: x**2
#uso de la funcion
base = 5
print(f"el cuadrado de {base} es: {cuadrado(5)}")

#Filtrado de lista con lambda
lista = [1, 2, 3, 4, 5, 6, 7, 8]
# Devuelve True si el numero es par
lambda par: par %2==0
# filter necesita un filtro y una lista a la que aplicarlo
filtrado = filter(lambda par: par %2==0,lista)
listaPares= list(filtrado)
print(f"Los pares de la lista son: {listaPares}")
#Lo anterior se puede hacer en una linea con: 
listaPares= list(filter(lambda par: par %2==0,lista))
print(f"Lista pares en una linea {listaPares}")

# Creacion de una nueva lista a partir de una existente, aplicando a cada elemento una funcion lambda
nuevaLista= list(map(lambda x: x*2, lista))
print(f"Lista x 2: {nuevaLista}")