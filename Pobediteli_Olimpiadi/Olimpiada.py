#Переменные
uchastniki = input("Напишите количество учинеков: ")
balls = input("Напишите количество правильных ответов у учеников через запятую: ")
balls1 = balls.split(", ")
winner = 0
debil_est = False
#Проверка на выход за рамки, а также поиск количества ответов у победителя
for pobeda in balls1:
    if int(pobeda) >= 20 and int(pobeda) != 20:
        print("ERROR")
        winner = 0
        break
    if int(pobeda) <= 0 and int(pobeda) != 0:
        print("ERROR")
        winner = 0
        break
    if int(uchastniki) <= 1 and int(uchastniki) != 1:
        print("ERROR")
        winner = 0
        break
    if int(uchastniki) >= 50 and int(uchastniki) != 50:
        print("ERROR")
        winner = 0
        break
    if winner <= int(pobeda) and int(pobeda) != winner:
        winner = 0
        winner += int(pobeda)
#Проверка есть ли человек который ничего не решил
for debil in balls1:
    if int(debil) == 0:
        debil_est = True
#Вывод результатов
if winner != 0:
    print(winner)
if winner != 0 and debil_est == True:
    print("YES")
if winner != 0 and debil_est == False:
    print("NO")
        
