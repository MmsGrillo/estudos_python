# -*- coding: utf-8 -*-
import random

minha_lista = ["Pera", "uva", "maçã", 1 , True, 8.8]
numeros = [5,66,632,23,56,65,5456,4563,2346,766345,323,12]
num = [0,1,2,3,4,5]
impar = [i for i in num if i%2==1]
par = [i for i in num if i%2==0]
goiabas = ["Goiaba"*3]*3
"""
numeros = sorted([5,66,632,23,56,65,5456,4563,2346,766345,323,12])

len(minha_lista)			#retorna quantidade de index
print(minha_lista[2])		#printa posição 3 da minha_lista
minha_lista[1] = "Goiaba"	#altera o index 1 para Goiaba
minha_lista.append("Limão")	#metodo append insere item na minha_lista	minha_lista += "limão"
del minha_lista[0:]			#deleta item da minha_lista no index 0 até o último
del minha_lista[:5]			#deleta item da minha_lista no primeiro index até o index 5
del minha_lista[:]			#deleta item da minha_lista no primeiro index até o último
del minha_lista[0]			#deleta item da minha_lista no index 0
numeros.reverse()			#inverte as posições do ultimo para o primeiro
numeros[::-1]				#inverte as posições do ultimo para o primeiro
numeros.sort()				#metodo sort ordena que numeros esteja em ordem crescente
numeros.sort(reverse=True)  #metodo sort sera revertido, deixando numeros descrecente
numeros = random.choice(minha_lista)#funçao seleciona item aleatorio da lista numeros
numeros = sorted(numeros)   #função sorted precisa estar declarado a uma variavel para retornar o valor em ordem crescente

for item in minha_lista:	#para cada item na minha lista, printa um item
	print(item)

if "Pera" in minha_lista:	#se Pera esta na minha lista, imprime Pera está na lista
	print ("Pera está na lista")
"""
print(minha_lista)
print(goiabas)
print(numeros)