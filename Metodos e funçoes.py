#Escreva uma função que calcula o volume de uma esfera dado seu raio (4*3,14*r**3/3)
def volume_esfera(raio):
	x = ((raio**3)*3.14*4)/3
	return x
print(volume_esfera(4))

vol_esf = lambda r: r**3*4*3.14/3
print(vol_esf(3))

#Escreva uma função que verifica se um número está em um determinado intervalo, inclusive o máximo e mínimo
def range_chk(num,min,max):
	x = list(range(min,max+1))
	return num in x
print(range_chk(1,1,5))

ran_chk = lambda num,min,max: num in range(min,max+1)
print(ran_chk(5,1,5))

#Escreva uma função que aceita uma string e calcule o número de maiúsculas e minúsculas
def up_low(s):
	up=0
	low=0
	for i in s:
		if i.isupper():
			up = up + 1
		elif i.islower():
			low+=1
	return up, low
print(up_low("Olá, Mundo"))
#Escreva uma função que receba uma lista e retorna uma nova lista com elementos esxclusivos da primeira
def sequencia(lista):
	lista = set(lista)
	return lista
print(sequencia([1,2,2,3,3,4,5]))

seq_n_repet = lambda lista: set(lista)
print(seq_n_repet([1,1,2,2,3,4,5]))

#Escreva uma função para multiplicar todos os números em uma lista
def mult_list(lista):
	tot = 1
	for i in lista:
		tot *= i
	return tot
print(mult_list([1,2,3,4]))

#Escreva uma função que verifica se uma strinf é palindrome ou não
def palindrome(texto):
	return texto == texto[::-1]
print(palindrome("arara"))
