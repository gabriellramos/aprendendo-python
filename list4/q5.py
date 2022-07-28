"""
    5. Leia um numero real e imprima a quinta parte deste numero
"""

import numbers

def five_part(num):
    if (isinstance(num, numbers.Number)):
        return num/5.0
    else:
        return "Nao eh um numero"


print (five_part(5.0))
print (five_part("oi"))
