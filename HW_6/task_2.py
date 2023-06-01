# Задача 32: Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

def between(minn: int, maxx: int, lst: list[int]):
    lstn = []
    for i in lst:
        if i <= maxx and i >= minn:
            lstn.append(i)
    print(*lstn)

minn = int(input("Input min value: "))
maxx = int(input("Input max value: "))

lst = [2, 4, 1, 543, 21, 12, 5]
between(minn, maxx, lst)

