# Решение четвертой задачи первого домашнего задания
"""
Задача 8: Требуется определить, можно ли от шоколадки 
размером n × m долек отломить k долек, 
если разрешается сделать один разлом по прямой между дольками 
(то есть разломить шоколадку на два прямоугольника).
*Пример:*

3 2 4 -> yes
3 2 1 -> no
"""

print("Input below size of chocolate n x m.")
n = int(input("n = "))
m = int(input("m = "))
k = int(input("Input count of parts, that you need: "))
if k < m * n and (k % m == 0 or k % n == 0):
    print(f"{n} {m} {k} -> yes")
else: print(f"{n} {m} {k} -> no")