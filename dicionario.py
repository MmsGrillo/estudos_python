# -*- coding: utf-8 -*-

"""Em Python, dicionários são arrays associativos,
ou seja, um determinado valor passa a ser vinculado a uma chave.
Se o dicionário tiver vários elementos, você pode usar laços para imprimi-los"""

dicionarioSite = {"Google" : ["google.com", "google.com.br"], "Yahoo": ["yahoo.com", "yahoo.com.br"] }

for site in dicionarioSite:
	print(site)
	print(dicionarioSite[site])