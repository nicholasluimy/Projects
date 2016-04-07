"""
Using Harlem J Brothers' formulae for e"""



from decimal import *
from math import pow, factorial
def nthe(n):
    getcontext().prec = n
    final = Decimal(0)
    for i in range(n):
        final += Decimal((2*i+1)/factorial(2*i))
    print(final)
    return final
    
