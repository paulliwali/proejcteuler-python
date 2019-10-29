def primeNumber(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def factorNumber(num):
    factors = []
    for i in range(2, int(round(num**(1/2), 0))):
        if num % i == 0:
            factors.append(i)
    factors.sort(reverse=True)
    return factors

def largestPrimefactorNumber(num):
    factors = factorNumber(num)
    for f in factors:
        if primeNumber(f):
            return f

print(largestPrimefactorNumber(600851475143))