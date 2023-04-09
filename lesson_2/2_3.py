"""
Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
"""

number = int(input('Введите целое число: '))
result = '1, '
tmp = 2
if number == 0:
    result = '1'
elif number == 1:
    result = '1, 2'
elif number == 2:
    result = '1, 2, 4'
else:
    while tmp < number:
        result += f'{tmp}, '
        tmp *= 2
print(f'{number} -> {result}')