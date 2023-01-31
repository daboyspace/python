# Задача №7. Решение в группах
# Дано натуральное число. Требуется определить,
# является ли год с данным номером високосным. Если
# год является високосным, то выведите YES, иначе
# выведите NO. Напомним, что в соответствии с
# григорианским календарем, год является
# високосным, если его номер кратен 4, но не кратен
# 100, а также если он кратен 400.
# Input: 2016
# Output: YES

# Год, который делится без остатка на 100 (например, 1900) является високосным годом только в том случае, если он также без остатка делится на 400.

# если год делится на 4 без остатка, но делится на 100 только с остатком, то он високосный, иначе — невисокосный, кроме случая, если он делится без остатка на 400 — тогда он всё равно високосный

year = int(input("Введите год: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("YES")
        else:  print("NO")
    else:
        print("YES")
else:
    print("NO")
    
# if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#     print("YES")
# else:
#     print("NO")