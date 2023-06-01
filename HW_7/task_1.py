# Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. 
# Поскольку разобраться в его кричалках не настолько просто, 
# насколько легко он их придумывает, Вам стоит написать программу. 
# Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) 
# в каждой фразе стихотворения одинаковое. Фраза может состоять из одного слова, 
# если во фразе несколько слов, то они разделяются дефисами. 
# Фразы отделяются друг от друга пробелами. 
# Стихотворение  Винни-Пух вбивает в программу с клавиатуры. 
# В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, 
# если с ритмом все не в порядке
# *Пример:*
# **Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да    
# **Вывод:** Парам пам-пам 

data = "пара-ра-Рам рам-пам-папам па-ра-па-да"
glasnie = "о, а, у, е, э, я, и, ю, я"
phrases = data.lower().split()
count_b = []

for i in phrases:
    find = list(glasnie.split(", "))
    for j in range(len(i)-1):
        if i[j] in find: 
            count_b.append(i.count(i[j])) 
            find.remove(i[j])

for i in range(len(count_b)-2):
    if count_b[i] == count_b[i+1]: 
        print("Парам пам-пам")
        break
    else: print("Пам парам")