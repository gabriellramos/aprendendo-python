"""
    funcao nao-recursiva para calcular superfatorial
"""

def fatorial(num:int) -> int:
    fat = 1
    if (num>1):
        while (num>1):
            fat*=num
            num-=1
        return fat
    else:
        return 1

def sf(num:int) -> int:
    res = 1
    # sf(num) = 1 * fat(num)[1...num]
    if (num>1):
        #print("sf({}) = ".format(num))
        for i in range(1,num+1):
            #print("{}! *".format(i))
            res = res * fatorial(i)

        return res
    else:
        return 1

#print(sf(4))