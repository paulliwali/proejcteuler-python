numList = []
sum = 0

for i in range(1000):
    if i % 3 == 0 or i % 5 == 0:
        numList.append(i)
    else:
        i+= 1

for i in numList:
    sum += i

print(sum)
