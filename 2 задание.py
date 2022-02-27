# 2. Записать в массив все числа в диапазоне от 1 до 500 кратные 5.
a = int(input('Начало: '))
b = int(input('Конец: '))
l = []
for i in range(a, b):
    if i % 5 == 0:
        l.append(i)
    print(l)