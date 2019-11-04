import math

def pythagorean(a, b):
    return math.sqrt(a**2 + b**2)

def required_for_thousand(a, b):
    return (1000 - a - b)

def find_triplet():
    for a in range(1, 1000):
        for b in range(1, 1000):
            print(a, b)
            c = pythagorean(a, b)
            if c == required_for_thousand(a, b):
                return (a, b, c)

triplet = find_triplet()
answer = triplet[0] * triplet[1] * triplet[2]
print(answer)
