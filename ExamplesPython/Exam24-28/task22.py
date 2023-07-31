# Задача 22:
# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа.
# n - кол-во элементов первого набора.
# m - кол-во элементов второго набора.


# def create_array(n, mn, mx):
#     import random
#     array = [random.randint(mn, mx) for _ in range(n)]
#     return array
def manual_array(nums):
    
    array = input("Введите элементы массива через пробел: ").split()
    return array

n = int(input('Кол-во элементов первого набора? -> '))
m = int(input('Кол-во элементов второго набора? -> '))
listing_1 = manual_array(n)
listing_2 = manual_array(m)
print(listing_1)
print(listing_2)

set_1 = set(listing_1)
set_2 = set(listing_2)

result = set_1 & set_2
print('Пересечение множеств - ', sorted(result), '\n')