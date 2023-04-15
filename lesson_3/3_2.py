import random

"""
Задача 18: Требуется найти в массиве A[1..N] самый близкий наименьший по величине элемент к заданному числу X. 
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  
строках записаны N целых чисел Ai. Последняя строка содержит число X

*Пример:*

5
    1 2 3 4 5
    6
    -> 5
"""

len_list = int(input('Введите длинну списка: '))
number = int(input('Введите число: '))
list_1 = [random.randint(1, 10) for i in range(len_list)]
result = 0
min_tmp = number
for i in list_1:
    if number - i == 1:
        result = i
        break
    elif number - i < min_tmp:
        result = i
print(f'{len_list}\n\t{list_1}\n\t{number}\n\t-> {result}')