# Задача 26:  
# Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии.
# *Пример:*

# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8 

def degrAB(a, b):
    if b == 0:
        return 1
    elif b == 1:
        return a
    return a * degrAB(a, b-1)

inpDate = input("Input A and B separated by spaces: ").split()
print(degrAB(list(map(int, inpDate))[0],list(map(int, inpDate))[1]))