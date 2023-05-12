# Задача 28: 
# Напишите рекурсивную функцию sum(a, b), 
# возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. 
# Также нельзя использовать циклы.
# *Пример:*

# 2 2
#     4 

def SumAB(a, b):
    if b == 0:
        return a
    return SumAB(a, b-1) + 1

inpDate = input("Input A and B separated by spaces: ").split()
print(SumAB(list(map(int, inpDate))[0],list(map(int, inpDate))[1]))
