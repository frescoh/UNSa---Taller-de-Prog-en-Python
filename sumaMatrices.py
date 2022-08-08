
import random

m = int(raw_input("cantidad filas: "))
n = int(raw_input("cantidad cols: "))

limiteDer = int(raw_input("limite derecho generador enteros: "))

if (m>0 and n>0 and limiteDer>0):
	matA = []
	matB = []
	

	for i in range(m):
		matA.append([])
		matB.append([])

		for j in range(n):
			elementA = random.randint(0, limiteDer)
			elementB = random.randint(0, limiteDer)
			matA[i].append(elementA)
			matB[i].append(elementB)
	
	matC = []
	for i in range(m):
		
		print " fila " + str(i) + " de A:" + str(matA[i])
		print " fila " + str(i) + " de B:" + str(matB[i])

		matC.append([])
		for j in range(n):
			matC[i].append(matA[i][j]+ matB[i][j])

		print " fila " + str(i) + " de C:" + str(matC[i])

else:
	print "error en la carga de parametros"



