# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai (можно использовать псевдогенерацию). 
# Последняя строка содержит число X.
# *Пример:*
# 5
# 7 -2 3 5 1
# 3
# -> 1

import random

countEl = int(input('Input count of elements: '))
lst = [random.randint(1, countEl) for i in range(countEl)]
print(*lst)
findEl = int(input('Input number for search: '))
for el in lst:
    if el == findEl:
        print(lst.count(el))
        break
    else: 
        print('Number not found')
        break