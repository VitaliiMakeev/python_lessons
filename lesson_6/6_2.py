import random

"""
Задача 32: Определить индексы элементов массива (списка), 
значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не 
больше заданного максимума)
"""


def index_el(a, b, array):
    result = [i for i in range(len(array)) if a < array[i] < b]
    return result


list_1 = [random.randint(1, 21) for i in range(10)]
n = int(input('Введите минимальную границу элемента: '))
m = int(input('Введите максимальную границу элемента: '))
print(index_el(n, m, list_1))