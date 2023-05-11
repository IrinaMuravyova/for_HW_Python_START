# Задача 18: 
# Требуется найти в массиве A самый близкий по величине элемент к заданному числу X. 
# Если таких элементов несколько, вы вывести один любой. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai (можно использовать псевдогенерацию). 
# Последняя строка содержит число X
# *Пример:*
# 5
# 7 -2 3 5 1
# 6
# -> 7

import random

countEl = int(input('Input count of elements: '))
lst = [random.randint(1, countEl) for i in range(countEl)]
print(*lst)
findEl = int(input('Input number for search: '))

dif = abs(lst[0] - findEl)
nearestEl = lst[0]

for el in lst:
    difNew = abs(el-findEl)
    if difNew < dif:
        dif = difNew
        nearestEl = el
print(nearestEl)