# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются 
# в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. 
# m — кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.

print("Input n and m:")
countSent1 = int(input())
countSent2 = int(input())

sent1 = sent2 =  list()

print("Input first sentence:")
for i in range(countSent1):
    sent1.append(int(input()))
print("Input second sentence:")
for i in range(countSent2):
    sent1.append(int(input()))

print(sorted((set(sent1)).union(set(sent2))))
