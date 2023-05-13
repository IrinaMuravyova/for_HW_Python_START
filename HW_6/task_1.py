# Задача 30:  Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

def progress(n: int, d: int, a1: int) -> list[int]:
    lst = [a1]
    for i in range(2, n):
        lst.append(a1 + (i - 1) * d)
    print(*lst)

n = int(input("Input count of elements: "))
d = int(input("Input difference: "))
a1 = int(input("Input first element (a1): "))

progress(n, d, a1)
