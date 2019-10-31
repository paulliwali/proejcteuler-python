def prime_number(num):
    if num == 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def factor_number(num):
    factors = []
    for i in range(2, int(round(num**(1/2), 0))):
        if num % i == 0:
            factors.append(i)
    factors.sort(reverse=True)
    return factors

def largestPrimefactorNumber(num):
    factors = factor_number(num)
    for f in factors:
        if prime_number(f):
            return f

print(largestPrimefactorNumber(600851475143))