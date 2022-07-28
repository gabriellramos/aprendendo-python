"""
    5. Leia um numero real e imprima a quinta parte deste numero
"""

import numbers

def five_part(num):
    if (isinstance(num, numbers.Number)):
        return num/5.0
    else:
        return "Nao eh um numero"

#testes manuais 
#print(five_part(5.0))
#print(five_part(5))
#print(five_part(5.455646464))
#print(five_part("5"))
#print(five_part('5.0'))


