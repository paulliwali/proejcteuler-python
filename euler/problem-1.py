def multiples_check(num):
    if ((num % 3) == 0 or (num % 5) == 0):
        print("True")
        return True
    else:
        print("False")
        return False

def loop_till(num):
    cumulative_sum = 0
    for i in range(1, num):
        if multiples_check(i):
            cumulative_sum += i
        print(cumulative_sum)

loop_till(1000)