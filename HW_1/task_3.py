# Решение третьей задачи первого домашнего задания
"""
Задача 6: Вы пользуетесь общественным транспортом? 
Вероятно, вы расплачивались за проезд и получали билет с номером. 
Счастливым билетом называют такой билет с шестизначным номером, 
где сумма первых трех цифр равна сумме последних трех. 
Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
Вам требуется написать программу, которая проверяет счастливость билета.
*Пример:*

385916 -> yes
123456 -> no
"""

ticketNumber = int(input("Input number of ticket: "))
if  len(str(ticketNumber)) != 6:
    print("Number is wrong. Enter six digit's number.")
elif int(ticketNumber / 100000) + int(ticketNumber / 10000 % 10)+int(ticketNumber / 1000 % 10) == int(ticketNumber % 1000 / 100) + int(ticketNumber % 100 / 10) + int(ticketNumber % 10):
        print(f'{ticketNumber} -> yes')
else: 
    print(f'{ticketNumber} -> no')

