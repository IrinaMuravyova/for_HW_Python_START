# *Задача 20: 
# * В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. 
# В случае с английским алфавитом очки распределяются так:
# A, E, I, O, U, L, N, S, T, R – 1 очко; 
# D, G – 2 очка; 
# B, C, M, P – 3 очка; 
# F, H, V, W, Y – 4 очка; 
# K – 5 очков; J, X – 8 очков; 
# Q, Z – 10 очков. 

# А русские буквы оцениваются так: 
# А, В, Е, И, Н, О, Р, С, Т – 1 очко; 
# Д, К, Л, М, П, У – 2 очка; 
# Б, Г, Ё, Ь, Я – 3 очка; 
# Й, Ы – 4 очка; 
# Ж, З, Х, Ц, Ч – 5 очков; 
# Ш, Э, Ю – 8 очков; 
# Ф, Щ, Ъ – 10 очков. 
# Напишите программу, которая вычисляет стоимость введенного пользователем слова. 
# Будем считать, что на вход подается только одно слово, 
# которое содержит либо только английские, либо только русские буквы.
# *Пример:*
# ноутбук
# 12

point1Eng = {'A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R'}
point2Eng = {'D', 'G'}
point3Eng = {'B', 'C', 'M', 'P'}
point4Eng = {'F', 'H', 'V', 'W', 'Y'}
point5Eng = {'K'}
point8Eng = {'J', 'X'}
point10Eng = {'Q', 'Z'}

point1Rus = {'А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т'}
point2Rus = {'Д', 'К', 'Л', 'М', 'П', 'У'}
point3Rus = {'Б', 'Г', 'Ё', 'Ь', 'Я'}
point4Rus = {'Й', 'Ы'}
point5Rus = {'Ж', 'З', 'Х', 'Ц', 'Ч'}
point8Rus = {'Ш', 'Э', 'Ю'}
point10Rus = {'Ф', 'Щ', 'Ъ'}

word = (input("Input your word: ")).upper()

sum = 0

for ch in word:
    charSet = set(ch)

    if charSet.intersection(point1Eng): sum += 1
    elif charSet.intersection(point2Eng): sum += 2
    elif charSet.intersection(point3Eng): sum += 3
    elif charSet.intersection(point4Eng): sum += 4
    elif charSet.intersection(point5Eng): sum += 5
    elif charSet.intersection(point8Eng): sum += 8
    elif charSet.intersection(point10Eng): sum += 10
    
    elif charSet.intersection(point1Rus): sum += 1
    elif charSet.intersection(point2Rus): sum += 2
    elif charSet.intersection(point3Rus): sum += 3
    elif charSet.intersection(point4Rus): sum += 4
    elif charSet.intersection(point5Rus): sum += 5
    elif charSet.intersection(point8Rus): sum += 8
    elif charSet.intersection(point10Rus): sum += 10

print(sum)