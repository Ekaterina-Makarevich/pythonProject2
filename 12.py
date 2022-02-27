import random

l = [random.randint(0,20) for _ in range(7)]
print(l)
cou = 0
cou2 = 0
for i in l:
    if i % 2 == 0:
        cou += 1
    else:
        cou2 += 1


