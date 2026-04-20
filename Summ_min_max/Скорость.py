Cars = input('Число машин:')
Speed = input('Скорости машин через запятую:')
Speed1 = Speed.split(", ")
opredelitel = 'NO'
Bspeed = 0
for n in Speed1:
    if int(Cars) <= 1 or int(Cars) >= 30:
        Cars = 0
        print('Ошибка')
        break
    if int(n) <= 1 or int(n) >= 300:
        Cars = 0
        print('Ошибка')
        break
    if int(n) >= Bspeed:
        Bspeed = 0
        Bspeed += int(n)
    if int(n) <= 30 and int(n) != 30:
        opredelitel = 'YES'
if int(Cars) != 0:
    print(Bspeed)
    print(opredelitel)
