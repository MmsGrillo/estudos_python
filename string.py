 # -*- coding: utf-8 -*-

a = "Murillo"
b = "Grillo"
lista = "Murillo Martiniano Grillo"
concatenar = (a+" "+b)

print (concatenar[0]) #imprime primeira posição
print (concatenar[1]) #imprime segunda posição
print (concatenar[2]) #imprime terceira posição
print (concatenar[3]) #imprime quarta posição
print (concatenar[4]) #imprime quinta posição
print (concatenar[5]) #imprime sexta posição
print (concatenar[6]) #imprime setima posição


print (concatenar[0:10]) #imprime 10 caracter a partir da posição 0

print (len (concatenar)) # função len conta a quantidade de caracter utiliza nas string

print (concatenar[0].lower()) #imprime primeira posição em minusculo
print (concatenar[1].upper()) #imprime segunda posição em maiusculo

print (lista.split()) #imprime separando ao termino de cada string
print (lista.split("i")) #imprime separando a cada string i

print (lista[lista.find("Ma"):30]) #imprime a partir da busca Ma até o caracter 30

print (lista.replace("Murillo", "Marcello")) #imprime Marcello onde estiver Murillo

