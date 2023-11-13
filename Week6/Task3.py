def checkPrime(val):
    for i in range(val-1,1,-1):
        if(val % i)==0:
            return False
    return True

print(checkPrime(1234567891))