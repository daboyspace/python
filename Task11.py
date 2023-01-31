# Задача №11. Решение в группах
# Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1.
# Input: 5
# Output: 6 

a = int(input("Введите число: "))

fib1 = 0
fib2 = 1
list1 = [0,1]
n = 2
while a > fib2:
    fib1,fib2 = fib2,fib1+fib2
    list1.append(fib2)
    n+=1
print(f'Числа фибоначи: \n {list1}')
print(f'Число {a} по счёту {n}-ое число Фибоначчи' if a == fib2 else f'Код -1: Число {a} не является числом Фибоначчи')