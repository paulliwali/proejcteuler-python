def sumOfSquares(digits):
    cumSum = 0
    for i in range(1, 10**digits+1):
        cumSum = cumSum + i**2
    return cumSum

def squareOfSum(digits):
    cumSum = 0
    for i in range(1, 10**digits+1):
        cumSum = cumSum + i
    return cumSum**2
    
print(squareOfSum(2) - sumOfSquares(2))