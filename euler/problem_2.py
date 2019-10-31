def fib(n):
    initial_num = 1
    i = 2
    fib = []
    fib_even_sum = 0
    fib.append(initial_num)
    while i < n:
        fib.append(i)
        intermediate_num = i
        i = i + initial_num
        initial_num = intermediate_num

    for i in fib:
        if i % 2 == 0:
            fib_even_sum += i
        print(fib_even_sum)

fib(4000001)
