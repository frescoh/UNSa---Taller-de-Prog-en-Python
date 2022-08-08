# aproximacion de mochila

import random

n = int(input("cantidad elementos: "))
pesoMaximo = int(input("peso maximo: "))

gananciaDer = int(input("maxima ganancia (rnd): "))
pesoDer = int(input("maximo peso (rnd): "))

if (n>0 and gananciaDer>0 and pesoDer>0 and pesoDer<pesoMaximo):
	solution = []
	weights = []
	benefits = []
	
	for i in range(n):		
		ganancia = random.randint(1, gananciaDer)
		peso = random.randint(1, pesoDer)

		weights.append(peso)
		benefits.append(ganancia)
	
	sumaBeneficio=0
	sumaPeso = 0
	ban=True
	while ban:		
		i = random.randint(0,n-1)		
		if i not in solution and sumaPeso + weights[i]<=pesoMaximo:
			solution.append(i)
			sumaPeso+=weights[i]
			sumaBeneficio+=benefits[i]
			
		else:
			ban=False
	
	print(" mochila " + str(solution))
	print(" beneficio " + str(sumaBeneficio))
	print(" beneficios " + str(benefits))
	print(" pesos " + str(weights))

else:
	print("error en la carga de parametros")



