# https://www.pitt.edu/~naraehan/python2/string_methods1.html
# https://www.programiz.com/python-programming/methods/string

x = input("ingrese una cadena de texto: ")

if x!="": 	# Analiza que la cadena no esté vacia
	y = "" 	
	for element in x:
		y = element + y      

	print("La cadena ingresada es: " + x)
	print("La cadena invertida es: " + y)
	
	# upper convierte la cadena en mayusculas, lower en minusculas,
	# capizalize pone la primera letra en mayusculas y el resto en minuscula
	print(" upper " +x.upper())
	print(" lower " +x.lower())
	print(" capitalize " +x.capitalize())
	
	# Devuelve True si es que todos los caracteres son digitos, False si hay al menos uno que no lo sea
	if x.isdigit():
		print("son todos digitos " + x)
	else:
		print("algunos caracteres no son digitos " + x)

	# en caso de que la contenga, index busca donde comienza una subcadena dentro de la cadena
	# Para evitar la excepcion en caso de que la subcadena no se encuentre en la cadena, se puede trabajar con el metodo find()
	# https://www.w3schools.com/python/ref_string_index.asp
	subC = input("ingrese subcadena a buscar dentro del texto ingresado anteriormente: ")
	if subC!="":
		print("La subC esta en posicion: " + x.index(subC))
		#str.index(sub[, start[, end]] )
	else:
		print("subcadena vacia. Reintente")
		
	
	lista = x.split(" ")
	# formo una lista con las palabras de la cadena
	#str.split([separator [, maxsplit]])
	
	print(lista)
	

else:
	print("cadena vacia. Reintente")
