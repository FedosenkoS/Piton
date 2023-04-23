# Задание 1. Задачи на одномерные списки
#
# Вариант 5
# Найдите наименьший четный элемент списка. Если такого нет, то выведите первый элемент.
# Преобразовать список так, чтобы сначала шли нулевые элементы, а затем все остальные.

import random

n = 15
a = [random.randrange(0, 10) for i in range(n)]

for i in range(n):
    print(a[i])

try:
    minimum = a[0]
    for i in range(1, len(a)):
        if a[i] < minimum and a[i]%2 == 0:
            minimum = a[i]
    print(f"Минимальный элемент списка {minimum}")

except:
    print(f"Минимальное четное значение не найдено. Первый элемент списка: {a[0]}")

print("Преобразованный список с нулевыми элементами вначале:")
b = 0
for i in range(0, len(a)):
    if a[i] == 0:
        a.pop(i)
        a.insert(b, 0)
        b += 1


for i in range(n):
    print(a[i])