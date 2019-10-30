def multiples_of_three_or_five(num):
    if ((num % 3) == 0 or (num % 5) == 0):
        return True
    else:
        return False

def cumulative_sum(num):
    cum_sum = 0
    for i in range(1, num):
        if multiples_of_three_or_five(i):
            cum_sum += i
    return cum_sum