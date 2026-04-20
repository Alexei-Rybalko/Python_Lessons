numbers = input("Введите числа через запятую и с нулем на конце: ")
num = numbers.split(", ")
del num[-1]
summa1 = 0
summa2 = 0
x = 30000
y = 0
z = 30000
o = 0
for i in num:
    if int(i) >= 30000 and int(i) <= -30000:
        print("Ошибка")
        summa1 = 0
        summa2 = 0
        x = 0
        y = 0
        break
    if int(i) <= x:
        x = 0
        x += int(i)
    if int(i) >= y:
        y = 0
        y += int(i)
for p in num:
    if int(p) >= 30000 and int(p) <= -30000:
        z = 0
        o = 0
        break
    if int(p) <= z and int(p) != x:
        z = 0
        z += int(p)
    if int(p) >= o and int(p) != y:
        o = 0
        o += int(p)
summa1 = y + o
summa2 = x + z
if summa1 != 0:
    print(summa1)
    print(summa2)
