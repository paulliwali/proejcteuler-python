from problem_3 import prime_number    

cum_sum = 0
for i in range(1, 2000000):
    if prime_number(i): cum_sum += i

print(cum_sum)