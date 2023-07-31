# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой,
# а некоторые – гербом. Определите минимальное число монеток, которые нужно
# перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть

# import random
# print("введите количество монеток всего")
# n = (int(input()))
# list_1=[]
# for i in range(n+1):
#     list_1.append(random.randrange(0,2))
# print (list_1)
# count=0             # count = 0
# for i in list_1:    # for i in range(len(list_1)):
#     if i==0:        #     if list_1[i] == k:
#         count+=1    #         count += 1
# print (count)       # print(count)   



#Ближайший элемент в массиве
# list_1 = [1, 2, 7, 5, 3, 4, 5]
# k = 5
# m = abs(k - list_1[0])  # модуль числа
# number = list_1[0]
# for i in range(1, len(list_1)):
#     if m > abs(list_1[i] - k):
#         m = abs(list_1[i] - k)
#         number = list_1[i]
# print(number)




# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000),
# а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих 
# чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

# S, P = (int(input()) for i in range(2))
# for y in range(1, 1001):
#     x=P/y
#     if (S*y-y*y)==P and x==S-y:
#         print (x,y)
#     elif y==1000 and (S*y-y*y)!=P:
#         print("нет решения")


# # Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), 
# # не превосходящие числа N.

# N=200
# list_1 = [i * 2 for i in range(1,N) if i*2 <=N]
# print (list_1)


# def fib(n):
#     if n in [1, 2]:
#         return 1
#     return fib(n - 1) + fib(n - 2)

# list_1 = []
# for i in range(1, 10):
#     list_1.append(fib(i - 2))
# print(list_1) # [1, 1, 2, 3, 5, 8, 13, 21, 34]

# Быстрая сортировка
# def quicksort(array):
#     if len(array) < 2:
#         return array
#     else:
#         pivot = array[0]
#         less = [i for i in array[1:] if i <= pivot]
#         greater = [i for i in array[1:] if i > pivot]
#         return quicksort(less) + [pivot] + quicksort(greater)
# print(quicksort([10, 5, 2, 3]))

# сортрировка слиянием
# def merge_sort(nums):
#     if len(nums) > 1:
#         mid = len(nums) // 2
#         left = nums[:mid]
#         right = nums[mid:]
#         merge_sort(left)
#         merge_sort(right)
#         i = j = k = 0
#         while i < len(left) and j < len(right):
#             if left[i] < right[j]:
#                 nums[k] = left[i]
#                 i += 1
#             else:
#                 nums[k] = right[j]
#                 j += 1
#             k += 1
#         while i < len(left):
#             nums[k] = left[i]
#             i += 1
#             k += 1
#         while j < len(right):
#             nums[k] = right[j]
#             j += 1
#             k += 1
    
# nums = [38, 27, 43, 3, 9, 82, 10]
# merge_sort(nums)
# print(nums)


# #SKRABL
# points_en = {1: 'AEIOULNSTR', 2: 'DG', 3: 'BCMP', 4: 'FHVWY', 5: 'K', 8: 'JX', 10: 'QZ'}
# points_ru = {1: 'АВЕИНОРСТ', 2: 'ДКЛМПУ', 3: 'БГЁЬЯ', 4: 'ЙЫ', 5: 'ЖЗХЦЧ', 8: 'ШЭЮ', 10: 'ФЩЪ'}
# word = input("input text: ").upper()  # переводим все буквы в верхний регистр
# count = 0
# for i in word:
#     if i in 'QWERTYUIOPASDFGHJKLZXCVBNM':
#         for j in points_en:
#             if i in points_en[j]:
#                 count = count + j
#     else:
#         for j in points_en:
#             if i in points_ru[j]:
#                 count = count + j
# print(count)

# text = input().split()
# count_char= {}
# for char in text:
#     if char not in count_char:
#         print(char, end="")
#         count_char[char] =1
#     else:
#         print(f'{char}_{count_char[char]}', end='')
#         count_char[char] +=1
# # a a a b c a a d c d d

print(len(set(input("input text ").lower().split())))#
