def isPalindromic(num):
    if str(num) == str(num)[::-1]:
        return True
    else:
        return False

def calcProduct(num1, num2):
    return (num1 * num2)

def largestPalindromic(digits):
    products = []
    for i in reversed(range(10 ** (digits-1), 10 ** digits)):
        for j in reversed(range(10 ** (digits-1), 10 ** digits)):
            products.append(calcProduct(i, j))
    products.sort(reverse = True)
    for p in products:
        if isPalindromic(p):
            return p

print(largestPalindromic(3))