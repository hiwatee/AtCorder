line = [input() for i in range(2)]

status = [int(x) for x in line[0].split()]
fruits = [int(x) for x in line[1].split()]

status
fruits = sorted(fruits)

i = 1
total = 0
for fruit in fruits:
    i += 1
    total += int(fruit)
    if int(status[1]) < i:
        break
print(total)
