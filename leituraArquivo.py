# -*- coding: utf-8 -*-

arquivo = open("meuArquivo.txt")	#cria variável de nome arquivo que abre "meuArquivo.txt"

#print(arquivo)						#imprime info do arquivo
#print(arquivo.read())				#imprime tudo dentro do arquivo como algo único
#print(arquivo.readline())			#imprime uma linha do arquivo de forma única
#print(arquivo.readlines())			#imprime todas as linhas de um arquivo como lista
for linha in arquivo.readlines():	#cria variavel linha.
	print (linha)					#para cada linha no arquivo, imprime linha

arquivo.close()						#fecha variavel arquivo