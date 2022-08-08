# ejemplo de diccionario

import random

banda = ['u2', 'rolling stones', 'simple minds', 'radiohead']

discoU2=['joshua tree', 'beautiful day', 'how to dismantle an atomic bom']
discoSimple = ['life in a day', 'real to real company', 'sons and fascination', 'sister feelings call']
discoRolling=['voodoo lounge', 'bridges to babylon', 'a bigger bang', 'blue and lonesone']
discoRadio=['the bends', 'kid A', 'ok computer', 'in rainbows']


runs = int(input("cantidad de corridas: "))
if (runs>0):
	
	ranking = {}	
	n = len(banda)
	
	for i in range(n):
		ranking[banda[i]]=0
		
	for i in range(runs):
		nroAleatorio = random.randint(0,n-1)
		
		cantidad = ranking[banda[nroAleatorio]]
		ranking[banda[nroAleatorio]] = cantidad +1
	
	top1=''
	cantidad=0
	for i in range(n):
		
		if ranking[banda[i]]>cantidad:
			cantidad = ranking[banda[i]]
			top1=banda[i]
			
	print('la banda mas escuchada es ' + top1 + '# ' +str(cantidad))
	
	print(ranking)
		
else:
	print('error en la carga de parametros')

	
	

