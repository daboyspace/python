# Задача 16: Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai
# . Последняя строка содержит число X
# 5
# 1 2 3 4 5
# 3
# -> 1
from random import randint

n = int(input('Введите размер списка:'))
list1 = [randint(1,n) for i in range(n)]
print(list1)
x = int(input('Введите число:'))
print(list1.count(x))