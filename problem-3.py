def primeNum(n):
    prime_num = [2]
    i = 3
    isPrime = False

    while i < n:
        for num in prime_num:
            if i % num == 0:
                isPrime = False
                break
            else:
                isPrime = True

        if isPrime:
             prime_num.append(i)

        isPrime = False
        i = i + 1
    return prime_num

def factors(num, array):
    n = num
    factor = []

    for f in array:
        if n % f == 0:
            factor.append(f)

    return factor


def largestPrimeFactor(n):
    prime_num = primeNum(n)
    prime_factors = factors(n, prime_num)

    return max(prime_factors)

print largestPrimeFactor(600851475143)
