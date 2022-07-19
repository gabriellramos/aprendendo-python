"""
    Formas de print em python
"""

from math import ceil


num = 10.3

print (ceil(num)) # retorna o menor valor inteiro contido na variavel
print ("{0}".format("1 - Oi")) # string formatada dentro de chaves
print ("%s" %("2 - Oi")) # string formatada por tipos de dados
print ("3 - Oi"+"!") # impressão concatenada
print ("4 -", "Oi","!",sep=" ") # impressão com separadores