# Задача 28:
# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.


def recursive_sum(a, b):
    if a == 0:
        return b
    else:
        a=a-1
        b=b+1
        return recursive_sum(a, b)

a = int(input('Введите А:'))
print()
b = int(input('Введите В:'))
print()

print(recursive_sum(a, b))