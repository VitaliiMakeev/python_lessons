import random

"""
Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

*Пример:*

5
    1 2 3 4 5
    3
    -> 1
"""
len_list = int(input('Введите длинну списка: '))
number = int(input('Введите искомое число: '))
list_1 = [random.randint(1, 10) for i in range(len_list)]
print(f'{len_list}\n\t{list_1}\n\t{number}\n\t-> {list_1.count(number)}')

