quantity = int(input("Количесто чисел: "))
numbers = input("Числа через запятую: ")
num = numbers.split(", ")
summa = 0
for i in num:
    if quantity >= 1000:
        print("Ошибка Eror Упся")
        summa = 0
        break
    if int(i) >= 30000:
        print("Ошибка Eror Упся")
        summa = 0
        break
    if i[-1] == '4' and int(i) % 6 == 0:
        summa += int(i)
if summa != 0:
    print(summa)
