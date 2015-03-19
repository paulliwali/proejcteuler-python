def primeNum(n):
    prime_num = [2]
    i = 3
    while i < n:
        for num in prime_num:
            if i % num == 0:
                break
            else:
                prime_num.append(i)
                break
        i = i + 1
    print prime_num

primeNum(10)
