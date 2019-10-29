def evenlyDivide(number, upper_number):
    i = 1
    while i <= upper_number:
        if number % i != 0:
            return False
        i += 1
    return True

def smallestNumber(upper_number, max_number):
    smallest_number = 1
    while smallest_number <= max_number:
        if evenlyDivide(smallest_number, upper_number):
            return smallest_number
        else:
            smallest_number += 1

    return smallest_number

print(smallestNumber(20, 9999999999))
    