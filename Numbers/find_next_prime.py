def is_prime(n):
    for i in range(2,n//2):
        if n%i == 0:
            return False
    if n//2 == 2:
        return False
    return True

def next_prime(n):
    n += 1
    if is_prime(n):
        return n
    else:
        return next_prime(n)

current = 1

while (1):
    
    proceed = input("Get next prime? (y/n)").lower()
    if (proceed == "y"):
        current = next_prime(current)
        print(current)
    elif (proceed =="n"):
        break
    else:
        print("Please enter a valid value")
