"""
    funcao para somar os algarismos de um numero:
    Ex.: 251 = 2+5+1 = 8
"""

def soma_algarismos(num:int):
    casa_decimal = 1
    #1, 10, 100, 1000, 10000, 10000
    while(num//casa_decimal!=0):
        casa_decimal = casa_decimal*10

    casa_decimal = casa_decimal/10
    #print("Algarismos do numero: {}".format(num))
    soma = 0
    div = num//casa_decimal
    while(div!=0):
        soma = soma+div
        resto = num % casa_decimal
        casa_decimal/=10
        #print("{0}".format(div))
        div = resto // casa_decimal
        resto = resto % casa_decimal

    return soma
   

#num = int(input("Digite um numero: "))
#print("Soma algarismos do valor {} = {}".format(num, soma_algarismos(num)))