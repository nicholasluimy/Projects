def nthfib(n):
    a  = 1
    b = 1
    print(a)
    for i in range(n-1):
        b = a+b
        a = b-a
        print(a)
    



