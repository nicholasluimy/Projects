"""
Using Bailey-Borwein-Plouffe formula to calculate pi to nth position accuracy
"""



from decimal import *
from math import pow
def nthpi(n):
    getcontext().prec = n
    final = Decimal(0)
    for i in range(n+1):
        final += Decimal(pow(16,-i))*(Decimal(4/(8*i+1))-Decimal(2/(8*i+4))
                                  -Decimal(1/(8*i+5))-Decimal(1/(8*i+6)))
    print(final)
    return final
    
