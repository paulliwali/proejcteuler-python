def isPrime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True 

def nThPrime(n):
    counter = 0
    i = 1
    while i > 0:
        if isPrime(i):
            if counter != n:
                counter += 1
            else: return i
        i += 1  

print(nThPrime(10001))
